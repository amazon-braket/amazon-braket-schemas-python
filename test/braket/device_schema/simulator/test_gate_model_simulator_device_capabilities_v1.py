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

from braket.device_schema.simulators.gate_model_simulator_device_capabilities_v1 import (
    GateModelSimulatorDeviceCapabilities,
)


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.simulators.gate_model_simulator_device_capabilities",
            "version": "1",
        },
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
            "shotsRange": [1, 10],
        },
        "action": {
            "braket.ir.jaqcd.program": {
                "actionType": "braket.ir.jaqcd.program",
                "version": ["1.0", "1.1"],
                "supportedOperations": ["x", "y"],
                "supportedResultTypes": [
                    {
                        "name": "resultType1",
                        "observables": ["observable1"],
                        "minShots": 2,
                        "maxShots": 4,
                    }
                ],
            }
        },
        "paradigm": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.simulators.gate_model_simulator_paradigm_properties",
                "version": "1",
            },
            "qubitCount": 32,
        },
        "deviceParameters": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.simulators.gate_model_simulator_device_parameters",
                "version": "1",
            },
            "paradigmParameters": {},
        },
        "device": {
            "supportedRegions": ["IAD"],
            "deviceCost": [10, "task"],
            "deviceMetadata": "metadata of the device",
            "deviceLocation": "IAD",
            "summary": "details of the device",
            "externalDocumentation": "details to external doc",
        },
    }
    return input


def test_valid(valid_input):
    result = GateModelSimulatorDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
    assert (
        result.braketSchemaHeader.name
        == "braket.device_schema.simulators.gate_model_simulator_device_capabilities"
    )


@pytest.mark.xfail(raises=ValidationError)
def test__missing_schemaHeader(valid_input):
    valid_input.pop("braketSchemaHeader")
    GateModelSimulatorDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_paradigm(valid_input):
    valid_input.pop("paradigm")
    GateModelSimulatorDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_deviceParameters(valid_input):
    valid_input.pop("deviceParameters")
    GateModelSimulatorDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_action(valid_input):
    valid_input.pop("action")
    GateModelSimulatorDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_service(valid_input):
    valid_input.pop("service")
    GateModelSimulatorDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
