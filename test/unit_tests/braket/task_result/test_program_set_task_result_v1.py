# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import pytest
from pydantic.v1 import ValidationError

from braket.ir.openqasm import Program
from braket.task_result.program_result_v1 import ProgramResult
from braket.task_result.program_set_executable_cancellation_v1 import (
    ProgramSetExecutableCancellationMetadata,
)
from braket.task_result.program_set_executable_failure_v1 import (
    FailureCategory,
    ProgramSetExecutableFailure,
    ProgramSetExecutableFailureMetadata,
)
from braket.task_result.program_set_executable_result_v1 import (
    ProgramSetExecutableResult,
    ProgramSetExecutableResultMetadata,
)
from braket.task_result.program_set_task_metadata_v1 import ProgramMetadata, ProgramSetTaskMetadata
from braket.task_result.program_set_task_result_v1 import ProgramSetTaskResult


@pytest.fixture
def valid_batch_executable_result():
    return ProgramSetExecutableResult(
        inputsIndex=0,
        measurements=[[0, 1], [1, 0]],
        measurementProbabilities={"00": 0.25, "01": 0.25, "10": 0.25, "11": 0.25},
        measuredQubits=[0, 1],
    )


@pytest.fixture
def valid_cancellation_metadata():
    return ProgramSetExecutableCancellationMetadata(status="CANCELLED")


@pytest.fixture
def valid_failure_metadata():
    return ProgramSetExecutableFailureMetadata(
        failureReason="Quantum circuit executable failed",
        retryable=True,
        category=FailureCategory.DEVICE.value,
    )


@pytest.fixture
def valid_executable_failure(valid_failure_metadata):
    return ProgramSetExecutableFailure(inputsIndex=0, failureMetadata=valid_failure_metadata)


@pytest.fixture
def valid_program_result(
    additional_metadata_gate_model, valid_batch_executable_result, valid_executable_failure
):
    return ProgramResult(
        source=Program(source="program", inputs={"param1": [0.5, 0.25]}),
        additionalMetadata=additional_metadata_gate_model,
        executableResults=["0.json", "1.json"],
    )


@pytest.fixture
def valid_program_result_local(
    additional_metadata_gate_model, valid_batch_executable_result, valid_executable_failure
):
    return ProgramResult(
        source="source.json",
        additionalMetadata=additional_metadata_gate_model,
        executableResults=[valid_batch_executable_result, valid_executable_failure],
    )


@pytest.fixture
def valid_program_metadata(valid_cancellation_metadata, valid_failure_metadata):
    return ProgramMetadata(
        executables=[
            ProgramSetExecutableResultMetadata(),
            valid_cancellation_metadata,
            ProgramSetExecutableResultMetadata(),
            valid_failure_metadata,
        ]
    )


@pytest.fixture
def valid_task_metadata(valid_program_metadata):
    return ProgramSetTaskMetadata(
        id="task_arn",
        requestedShots=100,
        successfulShots=100,
        deviceId="device_arn",
        programMetadata=[valid_program_metadata],
        deviceParameters={"paradigmParameters": {"qubitCount": 3, "disableQubitRewiring": True}},
        createdAt="created",
        endedAt="ended",
        status="COMPLETED",
        totalFailedExecutables=0,
    )


@pytest.fixture
def valid_task_result():
    return ProgramSetTaskResult(
        programResults=["programs/0/results.json", "programs/1/results.json"],
        s3Location=("amazon-braket-foo", "tasks/bar"),
        taskMetadata="metadata.json",
    )


@pytest.fixture
def valid_task_result_local(valid_program_result_local, valid_task_metadata):
    return ProgramSetTaskResult(
        programResults=[valid_program_result_local],
        s3Location=None,
        taskMetadata=valid_task_metadata,
    )


def test_valid_task_result(valid_task_result, valid_task_result_local):
    assert isinstance(valid_task_result, ProgramSetTaskResult)
    assert isinstance(valid_task_result_local, ProgramSetTaskResult)


def test_program_result_with_mixed_results(
    valid_batch_executable_result, valid_executable_failure, additional_metadata_gate_model
):
    subtask_result = ProgramResult(
        source=Program(source="program", inputs={"param1": [0.5, 0.25]}),
        additionalMetadata=additional_metadata_gate_model,
        executableResults=[valid_batch_executable_result, valid_executable_failure],
    )
    assert len(subtask_result.executableResults) == 2
    assert isinstance(subtask_result.executableResults[0], ProgramSetExecutableResult)
    assert isinstance(subtask_result.executableResults[1], ProgramSetExecutableFailure)


def test_missing_properties():
    with pytest.raises(ValidationError):
        ProgramSetTaskResult()


def test_empty_properties(valid_task_metadata):
    with pytest.raises(ValidationError):
        ProgramSetTaskResult(programResults=[])


def test_invalid_properties_results_type(valid_task_metadata):
    with pytest.raises(ValidationError):
        ProgramSetTaskResult(
            programResults="invalid", taskMetadata=valid_task_metadata, s3Location=None
        )


def test_invalid_missing_program_results(valid_task_metadata, additional_metadata_gate_model):
    with pytest.raises(ValidationError) as exc_info:
        ProgramSetTaskResult(
            programResults=None,  # Should be a list, not None
            taskMetadata=valid_task_metadata,
            s3Location=None,
        )
    assert "programResults" in str(exc_info.value)


def test_invalid_task_metadata_type(valid_program_result_local, additional_metadata_gate_model):
    with pytest.raises(ValidationError) as exc_info:
        ProgramSetTaskResult(
            programResults=[valid_program_result_local],
            taskMetadata=[],  # Should be BatchTaskMetadata, not list
            s3Location=None,
        )
    assert "taskMetadata" in str(exc_info.value)


def test_invalid_measurements(additional_metadata_gate_model):
    with pytest.raises(ValidationError) as exc_info:
        ProgramResult(
            source="source.json",
            additionalMetadata=additional_metadata_gate_model,
            executableResults=[
                ProgramSetExecutableResult(
                    inputsIndex=1,
                    measurements=["invalid"],  # Should be numeric strings
                    measurementProbabilities={"invalid": 1.0},
                    measuredQubits=[1],
                )
            ],
        )
    assert "measurements" in str(exc_info.value)


def test_invalid_device_parameters():
    with pytest.raises(ValidationError) as exc_info:
        ProgramSetTaskMetadata(
            id="task_arn",
            requestedShots=100,
            successfulShots=100,
            deviceId="device_arn",
            deviceParameters="invalid",  # Should be a dict
            createdAt=1,
            endedAt=2,
            status="COMPLETED",
            totalFailedExecutables=0,
        )
    assert "deviceParameters" in str(exc_info.value)
