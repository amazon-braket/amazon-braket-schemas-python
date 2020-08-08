# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

import json

import pytest
from pydantic import ValidationError

from braket.event_schema import BraketTaskStateChangeEvent


@pytest.mark.xfail(raises=ValidationError)
def test_missing_properties():
    BraketTaskStateChangeEvent()


def test_valid_event_deserialize(task_state_change_event_json):
    BraketTaskStateChangeEvent.parse_raw(json.dumps(task_state_change_event_json))


def test_valid_event_serialize(task_state_change_event_json):
    detail = {
        "quantumTaskArn": "some-arn",
        "status": "some-status",
        "deviceArn": "some-device",
        "shots": 10,
        "outputS3Bucket": "some-bucket",
        "outputS3KeyPrefix": "some-prefix",
        "createdAt": "2020-08-12T00:00:00.000Z",
    }
    if "endedAt" in task_state_change_event_json["detail"]:
        detail["endedAt"] = task_state_change_event_json["detail"]["endedAt"]
    event = BraketTaskStateChangeEvent(
        resources=["some-resource"], account="some-account", detail=detail,
    )
    # Exclude time because it's auto-generated
    assert (
        json.loads(event.json(exclude_none=True, exclude={"time"})) == task_state_change_event_json
    )


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_event_bad_source(bad_source_json):
    BraketTaskStateChangeEvent.parse_raw(json.dumps(bad_source_json))


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_event_bad_detail_type(bad_detail_type_for_task_state_change_json):
    BraketTaskStateChangeEvent.parse_raw(json.dumps(bad_detail_type_for_task_state_change_json))


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_event_bad_created_at(bad_created_at_for_task_state_change_json):
    BraketTaskStateChangeEvent.parse_raw(json.dumps(bad_created_at_for_task_state_change_json))
