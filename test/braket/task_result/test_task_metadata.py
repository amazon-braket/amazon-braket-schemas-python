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

from braket.task_result.task_metadata import TaskMetadata


@pytest.mark.xfail(raises=ValidationError)
def test_missing_properties(braket_schema_header):
    TaskMetadata(braketSchemaHeader=braket_schema_header)


def test_correct_metadata_minimum(braket_schema_header, id, device_id, shots):
    metadata = TaskMetadata(
        braketSchemaHeader=braket_schema_header, id=id, deviceId=device_id, shots=shots
    )
    assert metadata.id == id
    assert metadata.deviceId == device_id
    assert metadata.shots == shots
    assert TaskMetadata.parse_raw(metadata.json()) == metadata


def test_correct_metadata_all(braket_schema_header, id, device_id, shots):
    device_parameters = "{}"
    createdAt = "2020-01-02T03:04:05.006Z"
    endedAt = "2020-01-03T03:04:05.006Z"
    status = "COMPLETED"
    failureReason = "Foo"

    metadata = TaskMetadata(
        braketSchemaHeader=braket_schema_header,
        id=id,
        deviceId=device_id,
        shots=shots,
        deviceParameters=device_parameters,
        createdAt=createdAt,
        endedAt=endedAt,
        status=status,
        failureReason=failureReason,
    )
    assert metadata.id == id
    assert metadata.deviceId == device_id
    assert metadata.shots == shots
    assert metadata.deviceParameters == device_parameters
    assert metadata.createdAt == createdAt
    assert metadata.endedAt == endedAt
    assert metadata.status == status
    assert metadata.failureReason == failureReason
    assert TaskMetadata.parse_raw(metadata.json()) == metadata


@pytest.mark.parametrize("shots", [([1, 2]), (-1)])
@pytest.mark.xfail(raises=ValidationError)
def test_incorrect_shots(braket_schema_header, id, device_id, shots):
    TaskMetadata(braketSchemaHeader=braket_schema_header, id=id, deviceId=device_id, shots=shots)
