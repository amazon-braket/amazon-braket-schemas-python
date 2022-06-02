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

from braket.device_schema.xanadu.xanadu_device_capabilities_v1 import XanaduDeviceCapabilities


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.xanadu.xanadu_device_capabilities",
            "version": "1",
        },
        "service": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.device_service_properties",
                "version": "1",
            },
            "executionWindows": [
                {"executionDay": "Everyday", "windowStartHour": "11:00", "windowEndHour": "12:00"}
            ],
            "shotsRange": [1, 10],
            "deviceCost": {"price": 0.25, "unit": "minute"},
            "deviceDocumentation": {
                "imageUrl": "image_url",
                "summary": "Summary on the device",
                "externalDocumentationUrl": "exter doc link",
            },
            "deviceLocation": "us-east-1",
            "updatedAt": "2020-06-16T19:28:02.869136",
        },
        "action": {
            "braket.ir.blackbird.program": {
                "actionType": "braket.ir.blackbird.program",
                "version": ["1"],
                "supportedOperations": ["x", "y"],
                "supportedResultTypes": [],
            }
        },
        "paradigm": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.continuous_variable_qpu_paradigm_properties",
                "version": "1",
            },
            "modes": {"spatial": 1, "concurrent": 44, "temporal_max": 331},
            "layout": "Some layout",
            "compiler": ["borealis"],
            "supportedLanguages": ["blackbird:1.0"],
            "compilerDefault": "borealis",
            "nativeGateSet": ["XGate"],
            "gateParameters": {
                "s": [[0.0, 2.0]],
                "r0": [[-1.5707963267948966, 1.5707963267948966]],
            },
            "target": "borealis",
        },
        "deviceParameters": {},
    }
    return input


def test_valid(valid_input):
    result = XanaduDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
    assert (
        result.braketSchemaHeader.name == "braket.device_schema.xanadu.xanadu_device_capabilities"
    )


@pytest.mark.xfail(raises=ValidationError)
def test__missing_schemaHeader(valid_input):
    valid_input.pop("braketSchemaHeader")
    XanaduDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_paradigm(valid_input):
    valid_input.pop("paradigm")
    XanaduDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_deviceParameters(valid_input):
    valid_input.pop("deviceParameters")
    XanaduDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_action(valid_input):
    valid_input.pop("action")
    XanaduDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_service(valid_input):
    valid_input.pop("service")
    XanaduDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
