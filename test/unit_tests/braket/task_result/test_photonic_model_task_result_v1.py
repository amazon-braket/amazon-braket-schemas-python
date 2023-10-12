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

from braket.task_result.photonic_model_task_result_v1 import PhotonicModelTaskResult


@pytest.fixture
def measured_qubits():
    return [0, 1]


@pytest.fixture(params=[([[[0, 220]], [[100, 122]]]), [[[100]], [[100]]]])
def measurements(request):
    return request.param


@pytest.mark.xfail(raises=ValidationError)
def test_missing_properties():
    PhotonicModelTaskResult()


@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_header(
    braket_schema_header,
    task_metadata,
    additional_metadata_photonic_model,
    measurements,
):
    PhotonicModelTaskResult(
        braketSchemaHeader=braket_schema_header,
        measurements=measurements,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_photonic_model,
    )


def test_correct_result_measurements(
    task_metadata,
    additional_metadata_photonic_model,
    measurements,
):
    result = PhotonicModelTaskResult(
        measurements=measurements,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_photonic_model,
    )
    assert result.measurements == measurements
    assert result.taskMetadata == task_metadata
    assert result.additionalMetadata == additional_metadata_photonic_model
    assert PhotonicModelTaskResult.parse_raw(result.json()) == result
    assert result == PhotonicModelTaskResult.parse_raw_schema(result.json())


@pytest.mark.parametrize(
    "measurements", [([]), ([[]]), ([[-1]]), ([[2]]), ([[220, 100]]), ([[[-1]], [[300]]])]
)
@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_measurements(
    measurements,
    measured_qubits,
    task_metadata,
    additional_metadata_photonic_model,
):
    PhotonicModelTaskResult(
        measurements=measurements,
        measuredQubits=measured_qubits,
        taskMetadata=task_metadata,
        additionalMetadata=additional_metadata_photonic_model,
    )
