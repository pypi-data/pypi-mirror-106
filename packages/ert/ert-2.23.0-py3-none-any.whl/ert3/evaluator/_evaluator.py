import asyncio
import os
import pathlib
import shutil
import typing
from collections import defaultdict

import cloudpickle
import ert3
from ert_shared.ensemble_evaluator.config import EvaluatorServerConfig
from ert_shared.ensemble_evaluator.evaluator import EnsembleEvaluator
from ert_shared.ensemble_evaluator.prefect_ensemble import PrefectEnsemble

_EVTYPE_SNAPSHOT_STOPPED = "Stopped"
_EVTYPE_SNAPSHOT_FAILED = "Failed"


def _create_evaluator_tmp_dir(workspace_root, evaluation_name):
    return (
        pathlib.Path(workspace_root)
        / ert3._WORKSPACE_DATA_ROOT
        / "tmp"
        / evaluation_name
    )


def _prepare_input(
    ee_config,
    step_config: ert3.config.Step,
    inputs: ert3.data.MultiEnsembleRecord,
    evaluation_tmp_dir,
    ensemble_size,
) -> typing.Dict[int, typing.Dict[str, ert3.data.RecordTransmitter]]:
    tmp_input_folder = evaluation_tmp_dir / "prep_input_files"
    os.makedirs(tmp_input_folder)
    storage_config = ee_config["storage"]
    transmitters: typing.Dict[
        int, typing.Dict[str, ert3.data.RecordTransmitter]
    ] = defaultdict(dict)

    futures = []
    for input_ in step_config.input:
        for iens, record in enumerate(inputs.ensemble_records[input_.record].records):
            if storage_config.get("type") == "shared_disk":
                transmitter = ert3.data.SharedDiskRecordTransmitter(
                    name=input_.record,
                    storage_path=pathlib.Path(storage_config["storage_path"]),
                )
            else:
                raise ValueError(
                    f"Unsupported transmitter type: {storage_config.get('type')}"
                )
            futures.append(transmitter.transmit_data(record.data))
            transmitters[iens][input_.record] = transmitter
    asyncio.get_event_loop().run_until_complete(asyncio.gather(*futures))
    if step_config.transportable_commands is not None:
        for command in step_config.transportable_commands:
            if storage_config.get("type") == "shared_disk":
                transmitter = ert3.data.SharedDiskRecordTransmitter(
                    name=command.name,
                    storage_path=pathlib.Path(storage_config["storage_path"]),
                )
            else:
                raise ValueError(
                    f"Unsupported transmitter type: {storage_config.get('type')}"
                )
            with open(command.location, "rb") as f:
                asyncio.get_event_loop().run_until_complete(
                    transmitter.transmit_data([f.read()])
                )
            for iens in range(0, ensemble_size):
                transmitters[iens][command.name] = transmitter
    return dict(transmitters)


def _prepare_output(
    ee_config,
    step_config: ert3.config.Step,
    evaluation_tmp_dir: pathlib.Path,
    ensemble_size: int,
) -> typing.Dict[int, typing.Dict[str, ert3.data.RecordTransmitter]]:
    tmp_input_folder = evaluation_tmp_dir / "output_files"
    os.makedirs(tmp_input_folder)
    storage_config = ee_config["storage"]
    transmitters: typing.Dict[
        int, typing.Dict[str, ert3.data.RecordTransmitter]
    ] = defaultdict(dict)

    for output in step_config.output:
        for iens in range(0, ensemble_size):
            if storage_config.get("type") == "shared_disk":
                transmitters[iens][
                    output.record
                ] = ert3.data.SharedDiskRecordTransmitter(
                    name=output.record,
                    storage_path=pathlib.Path(storage_config["storage_path"]),
                )
            else:
                raise ValueError(
                    f"Unsupported transmitter type: {storage_config.get('type')}"
                )
    return dict(transmitters)


def _build_ee_config(
    evaluation_tmp_dir,
    ensemble,
    stages_config: ert3.config.StagesConfig,
    input_records: ert3.data.MultiEnsembleRecord,
    dispatch_uri: str,
):
    if ensemble.size != None:
        ensemble_size = ensemble.size
    else:
        ensemble_size = input_records.ensemble_size

    stage = stages_config.step_from_key(ensemble.forward_model.stage)
    assert stage is not None
    commands = stage.transportable_commands if stage.transportable_commands else []
    output_locations = [out.location for out in stage.output]
    jobs = []

    def command_location(name):
        try:
            return next(
                cmd.location for cmd in stage.transportable_commands if cmd.name == name
            )
        except StopIteration:
            return pathlib.Path(name)

    if stage.function:
        jobs.append(
            {
                "name": stage.function.__name__,
                "executable": cloudpickle.dumps(stage.function),
                "output": output_locations[0],
            }
        )

    if stage.script is not None:
        for script in stage.script:
            name, *args = script.split()
            jobs.append(
                {
                    "name": name,
                    "executable": command_location(name),
                    "args": tuple(args),
                }
            )

    steps = [
        {
            "name": stage.name + "-only_step",
            "inputs": [
                {
                    "record": input_.record,
                    "location": input_.location,
                    "mime": input_.mime,
                    "is_executable": False,
                }
                for input_ in stage.input
            ]
            + [
                {
                    "record": cmd.name,
                    "location": command_location(cmd.name),
                    "mime": cmd.mime,
                    "is_executable": True,
                }
                for cmd in commands
            ],
            "outputs": [
                {
                    "record": output.record,
                    "location": output.location,
                    "mime": output.mime,
                }
                for output in stage.output
            ],
            "jobs": jobs,
            "type": "function" if stage.function else "unix",
        }
    ]

    ee_config = {
        "steps": steps,
        "realizations": ensemble_size,
        "max_running": 10000,
        "max_retries": 0,
        "run_path": evaluation_tmp_dir / "my_output",
        "executor": ensemble.forward_model.driver,
        "storage": {
            "type": "shared_disk",
            "storage_path": evaluation_tmp_dir / ".my_storage",
        },
        "dispatch_uri": dispatch_uri,
    }

    ee_config["inputs"] = _prepare_input(
        ee_config, stage, input_records, evaluation_tmp_dir, ensemble_size
    )
    ee_config["outputs"] = _prepare_output(
        ee_config, stage, evaluation_tmp_dir, ensemble_size
    )

    return ee_config


def _run(ensemble_evaluator):
    result = None
    with ensemble_evaluator.run() as monitor:
        for event in monitor.track():
            if event.data is not None and event.data.get("status") in [
                _EVTYPE_SNAPSHOT_STOPPED,
                _EVTYPE_SNAPSHOT_FAILED,
            ]:
                if event.data.get("status") == _EVTYPE_SNAPSHOT_STOPPED:
                    result = monitor.get_result()
                monitor.signal_done()
    return result


def _prepare_responses(raw_responses):
    async def _load(iens, record_key, transmitter):
        record = await transmitter.load()
        return (iens, record_key, record)

    futures = []
    for iens in sorted(raw_responses.keys(), key=int):
        for record, transmitter in raw_responses[iens].items():
            futures.append(_load(iens, record, transmitter))
    results = asyncio.get_event_loop().run_until_complete(asyncio.gather(*futures))

    data_results = defaultdict(dict)
    for res in results:
        data_results[res[0]][res[1]] = res[2]

    responses = {response_name: [] for response_name in data_results[0]}
    for realization in data_results.values():
        assert responses.keys() == realization.keys()
        for key in realization:
            responses[key].append(realization[key])

    for key in responses:
        responses[key] = ert3.data.EnsembleRecord(records=responses[key])

    return ert3.data.MultiEnsembleRecord(ensemble_records=responses)


def evaluate(
    workspace_root, evaluation_name, input_records, ensemble_config, stages_config
):
    evaluation_tmp_dir = _create_evaluator_tmp_dir(workspace_root, evaluation_name)

    config = EvaluatorServerConfig()
    ee_config = _build_ee_config(
        evaluation_tmp_dir,
        ensemble_config,
        stages_config,
        input_records,
        config.dispatch_uri,
    )
    ensemble = PrefectEnsemble(ee_config)

    ee = EnsembleEvaluator(ensemble=ensemble, config=config, iter_=0)
    result = _run(ee)
    responses = _prepare_responses(result)

    return responses


def cleanup(workspace_root, evaluation_name):
    tmp_dir = _create_evaluator_tmp_dir(workspace_root, evaluation_name)
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
