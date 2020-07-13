# Copyright 2019-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
from pydantic import ValidationError

from braket.ir.jaqcd.results import Probability
from braket.task_result.gate_model_task_result import GateModelTaskResult, ResultType


@pytest.fixture
def measured_qubits():
    return [0, 1]


@pytest.fixture
def measurements():
    return [[1, 0], [1, 0]]


@pytest.fixture
def measurement_probabilities():
    return {"10": 0.50, "01": 0.50}


@pytest.fixture
def result_types():
    return [
        ResultType(type=Probability(targets=[0]), value=[0.5, 0.5]),
        ResultType(type=Probability(targets=[1]), value=[0.5, 0.5]),
    ]


@pytest.mark.xfail(raises=ValidationError)
def test_missing_properties():
    GateModelTaskResult()


def test_correct_result_measurements(
    braket_schema_header,
    task_metadata,
    additional_metadata_gate_model,
    measured_qubits,
    measurements,
):
    result = GateModelTaskResult(
        braketSchemaHeader=braket_schema_header,
        measurements=measurements,
        measuredQubits=measured_qubits,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_gate_model,
    )
    assert result.measurements == measurements
    assert result.measuredQubits == measured_qubits
    assert result.taskMetadata == task_metadata
    assert result.additionalMetadata == additional_metadata_gate_model
    assert GateModelTaskResult.parse_raw(result.json()) == result


def test_correct_result_measurement_probabilities(
    braket_schema_header,
    task_metadata,
    additional_metadata_gate_model,
    measured_qubits,
    measurement_probabilities,
):
    result = GateModelTaskResult(
        braketSchemaHeader=braket_schema_header,
        measurementProbabilities=measurement_probabilities,
        measuredQubits=measured_qubits,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_gate_model,
    )
    assert result.measurementProbabilities == measurement_probabilities
    assert GateModelTaskResult.parse_raw(result.json()) == result


def test_correct_result_types(
    braket_schema_header,
    task_metadata,
    additional_metadata_gate_model,
    measured_qubits,
    result_types,
):
    result = GateModelTaskResult(
        braketSchemaHeader=braket_schema_header,
        resultTypes=result_types,
        measuredQubits=measured_qubits,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_gate_model,
    )
    assert result.resultTypes == result_types
    assert GateModelTaskResult.parse_raw(result.json()) == result


@pytest.mark.parametrize("measured_qubits", [([]), ([-1])])
@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_measured_qubits(
    measured_qubits, braket_schema_header, task_metadata, additional_metadata_gate_model
):
    GateModelTaskResult(
        braketSchemaHeader=braket_schema_header,
        measurementProbabilities=measurement_probabilities,
        measuredQubits=measured_qubits,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_gate_model,
    )


@pytest.mark.parametrize("measurements", [([]), ([[]]), ([[-1]]), ([[2]])])
@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_measurements(
    measurements,
    measured_qubits,
    braket_schema_header,
    task_metadata,
    additional_metadata_gate_model,
):
    GateModelTaskResult(
        braketSchemaHeader=braket_schema_header,
        measurements=measurements,
        measuredQubits=measured_qubits,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_gate_model,
    )


@pytest.mark.parametrize("measurement_probabilities", [({"hello": 0.5}), ({"01": 2})])
@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_measurement_probabilities(
    measurement_probabilities,
    measured_qubits,
    braket_schema_header,
    task_metadata,
    additional_metadata_gate_model,
):
    GateModelTaskResult(
        braketSchemaHeader=braket_schema_header,
        measurementProbabilities=measurement_probabilities,
        measuredQubits=measured_qubits,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_gate_model,
    )


@pytest.mark.parametrize("result_types", [([1, 2, 3]), (3)])
@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_result_types(
    braket_schema_header,
    task_metadata,
    additional_metadata_gate_model,
    measured_qubits,
    result_types,
):
    GateModelTaskResult(
        braketSchemaHeader=braket_schema_header,
        resultTypes=result_types,
        measuredQubits=measured_qubits,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_gate_model,
    )


@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_result_type_attribute_type():
    ResultType(type={"type": "unknown"}, value=[0.5, 0.5])


@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_result_type_attribute_value():
    ResultType(type={"type": "unknown"}, value=1)
