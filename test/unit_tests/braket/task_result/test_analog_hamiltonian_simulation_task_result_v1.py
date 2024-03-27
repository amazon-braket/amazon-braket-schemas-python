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

from braket.task_result.analog_hamiltonian_simulation_task_result_v1 import (
    AnalogHamiltonianSimulationShotMeasurement,
    AnalogHamiltonianSimulationShotMetadata,
    AnalogHamiltonianSimulationShotResult,
    AnalogHamiltonianSimulationTaskResult,
)


@pytest.fixture
def shot_status():
    return "Success"


@pytest.fixture
def pre_sequence():
    return [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]


@pytest.fixture
def post_sequence():
    return [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0]


@pytest.fixture
def shot_metadata():
    return AnalogHamiltonianSimulationShotMetadata(shotStatus="Success")


@pytest.fixture
def shot_result():
    return AnalogHamiltonianSimulationShotResult(
        preSequence=[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        postSequence=[0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
    )


@pytest.fixture
def ahs_measurements():
    return [
        AnalogHamiltonianSimulationShotMeasurement(
            shotMetadata=AnalogHamiltonianSimulationShotMetadata(shotStatus="Success"),
            shotResult=AnalogHamiltonianSimulationShotResult(
                preSequence=[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                post_sequence=[0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
            ),
        )
    ]


def test_correct_analogHamiltonianSimulationShotMetadata(
    shot_status,
):
    result = AnalogHamiltonianSimulationShotMetadata(
        shotStatus=shot_status,
    )
    assert result.shotStatus == shot_status


@pytest.mark.xfail(raises=ValidationError)
def test_missing_value_analogHamiltonianSimulationShotMetadata():
    AnalogHamiltonianSimulationShotMetadata(
        shotStatus=None,
    )


def test_correct_analogHamiltonianSimulationShotResult(
    pre_sequence,
    post_sequence,
):
    result = AnalogHamiltonianSimulationShotResult(
        preSequence=pre_sequence, postSequence=post_sequence
    )
    assert result.preSequence == pre_sequence
    assert result.postSequence == post_sequence


def test_optional_value_analogHamiltonianSimulationShotResult(
    pre_sequence,
    post_sequence,
):
    result = AnalogHamiltonianSimulationShotResult(postSequence=post_sequence)
    assert result.postSequence == post_sequence


def test_correct_analogHamiltonianSimulationShotMeasurement(
    shot_metadata,
    shot_result,
):
    result = AnalogHamiltonianSimulationShotMeasurement(
        shotMetadata=shot_metadata, shotResult=shot_result
    )
    assert result.shotMetadata == shot_metadata
    assert result.shotResult == shot_result


@pytest.mark.xfail(raises=ValidationError)
def test_missing_value_analogHamiltonianSimulationShotMeasuremen(
    shot_metadata,
    shot_result,
):
    AnalogHamiltonianSimulationShotMeasurement(
        shotMetadata=shot_metadata,
    )


def test_correct_analogHamiltonianSimulationTaskResult(
    task_metadata,
    ahs_measurements,
    additional_metadata_ahs,
):
    result = AnalogHamiltonianSimulationTaskResult(
        measurements=ahs_measurements,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_ahs,
    )
    assert result.taskMetadata == task_metadata
    assert result.measurements == ahs_measurements
    assert result.additionalMetadata == additional_metadata_ahs
    assert AnalogHamiltonianSimulationTaskResult.parse_raw(result.json()) == result
    assert result == AnalogHamiltonianSimulationTaskResult.parse_raw_schema(result.json())


def test_optional_value_analogHamiltonianSimulationTaskResult(task_metadata):
    result = AnalogHamiltonianSimulationTaskResult(
        taskMetadata=task_metadata,
    )
    assert result.taskMetadata == task_metadata
    assert AnalogHamiltonianSimulationTaskResult.parse_raw(result.json()) == result
    assert result == AnalogHamiltonianSimulationTaskResult.parse_raw_schema(result.json())


@pytest.mark.xfail(raises=ValidationError)
def test_missing_required_value_analogHamiltonianSimulationTaskResult(
    task_metadata,
    ahs_measurements,
):
    AnalogHamiltonianSimulationTaskResult(
        measurements=ahs_measurements,
    )
