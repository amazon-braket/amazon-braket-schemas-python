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

import pytest

from braket.event_schema import TASK_STATE_CHANGE_DETAIL_TYPE


@pytest.fixture(params=[None, "2020-08-12T00:00:00.000Z"])
def ended_at(request):
    return request.param


@pytest.fixture
def detail_for_task_state_change_json(ended_at):
    detail = {
        "braketSchemaHeader": {"name": "braket.event.task.state_change", "version": "1.0"},
        "quantumTaskArn": "some-arn",
        "status": "some-status",
        "deviceArn": "some-device",
        "shots": 10,
        "outputS3Bucket": "some-bucket",
        "outputS3KeyPrefix": "some-prefix",
        "createdAt": "2020-08-12T00:00:00.000Z",
    }
    if ended_at is not None:
        detail["endedAt"] = ended_at
    return detail


@pytest.fixture
def task_state_change_event_json(detail_for_task_state_change_json):
    return {
        "resources": ["some-resource"],
        "account": "some-account",
        "source": "aws.braket",
        "detailType": TASK_STATE_CHANGE_DETAIL_TYPE,
        "detail": detail_for_task_state_change_json,
    }


@pytest.fixture
def bad_source_json(task_state_change_event_json):
    bad_event = task_state_change_event_json
    bad_event["source"] = "invalid_source"
    return bad_event


@pytest.fixture
def bad_detail_type_for_task_state_change_json(task_state_change_event_json):
    bad_event = task_state_change_event_json
    bad_event["detailType"] = "invalid_detail_type"
    return bad_event


@pytest.fixture
def bad_created_at_for_task_state_change_json(task_state_change_event_json):
    bad_event = task_state_change_event_json
    bad_event["detail"]["createdAt"] = "invalid_created_at"
    return bad_event
