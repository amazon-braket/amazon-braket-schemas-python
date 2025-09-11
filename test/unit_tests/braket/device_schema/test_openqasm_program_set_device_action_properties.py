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
from pydantic.v1 import ValidationError

from braket.device_schema.openqasm_program_set_device_action_properties import (
    OpenQASMProgramSetDeviceActionProperties,
)


@pytest.fixture()
def valid_input():
    input = {
        "actionType": "braket.ir.openqasm.program_set",
        "version": ["1"],
        "maximumExecutables": 500,
        "maximumTotalShots": 1_000_000,
    }
    return input


def test_valid(valid_input):
    result = OpenQASMProgramSetDeviceActionProperties.parse_raw(json.dumps(valid_input))
    assert result.actionType == "braket.ir.openqasm.program_set"
    assert result.maximumExecutables == 500
    assert result.maximumTotalShots == 1_000_000


@pytest.mark.xfail(raises=ValidationError)
def test_missing_action_type(valid_input):
    valid_input.pop("actionType")
    OpenQASMProgramSetDeviceActionProperties.parse_raw(json.dumps(valid_input))


@pytest.mark.parametrize("field", ["maximumExecutables", "maximumTotalShots"])
@pytest.mark.xfail(raises=ValidationError)
def test_missing_field(valid_input, field):
    valid_input.pop(field)
    OpenQASMProgramSetDeviceActionProperties.parse_raw(json.dumps(valid_input))


@pytest.mark.parametrize("field", ["maximumExecutables", "maximumTotalShots"])
@pytest.mark.xfail(raises=ValidationError, reason="ensure this value is greater than or equal to 0")
def test_negative_field(valid_input, field):
    valid_input[field] = -1
    OpenQASMProgramSetDeviceActionProperties.parse_raw(json.dumps(valid_input))
