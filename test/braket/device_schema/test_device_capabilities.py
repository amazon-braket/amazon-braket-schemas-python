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

import json

import pytest
from pydantic import ValidationError

from braket.device_schema.device_capabilities import DeviceCapabilities


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "service": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.device_service_properties",
                "version": "1",
            },
            "executionWindows": [
                {
                    "executionDay": "Everyday",
                    "windowStartHour": "1966280412345.6789",
                    "windowEndHour": "1966280414345.6789",
                }
            ],
            "shots": 2,
        },
        "action": {
            "braket.ir.jaqcd.program": {
                "actionType": "braket.ir.jaqcd.program",
                "version": ["1.0", "1.1"],
            }
        },
        "paradigm": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.device_paradigm_properties",
                "version": "1",
            }
        },
        "deviceParameters": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.device_parameters",
                "version": "1",
            },
            "deviceParameters": {
                "braketSchemaHeader": {
                    "name": "braket.device_schema.annealing_model_parameters",
                    "version": "1",
                },
                "dwaveParameters": {
                    "braketSchemaHeader": {
                        "name": "braket.device_schema.dwave_parameters",
                        "version": "1",
                    }
                },
            },
        },
    }
    return input


def test_valid(valid_input):
    assert DeviceCapabilities.parse_raw(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_paradigm(valid_input):
    valid_input.pop("paradigm")
    DeviceCapabilities.parse_raw(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_deviceParameters(valid_input):
    valid_input.pop("deviceParameters")
    DeviceCapabilities.parse_raw(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_action(valid_input):
    valid_input.pop("action")
    DeviceCapabilities.parse_raw(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_service(valid_input):
    valid_input.pop("service")
    DeviceCapabilities.parse_raw(json.dumps(valid_input))
