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

import json

import pytest
from pydantic import ValidationError

from braket.device_schema.blackbird_device_action_properties import BlackbirdDeviceActionProperties


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "actionType": "braket.ir.blackbird.program",
        "version": ["1"],
        "supportedOperations": ["BSGate", "XGate"],
        "supportedResultTypes": [],
    }
    return input


def test_valid(valid_input):
    result = BlackbirdDeviceActionProperties.parse_raw(json.dumps(valid_input))
    assert result.actionType == "braket.ir.blackbird.program"
    assert result.supportedOperations == ["BSGate", "XGate"]
    assert result.supportedResultTypes == []


@pytest.mark.xfail(raises=ValidationError)
def test_missing_action_type(valid_input):
    valid_input.pop("actionType")
    BlackbirdDeviceActionProperties.parse_raw(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_supported_operations(valid_input):
    valid_input.pop("supportedOperations")
    BlackbirdDeviceActionProperties.parse_raw(json.dumps(valid_input))
