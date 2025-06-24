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

from braket.device_schema.error_mitigation import Debias
from braket.device_schema.ionq.ionq_device_capabilities_v1 import IonqDeviceCapabilities

jaqcd_valid_input = {
    "braketSchemaHeader": {
        "name": "braket.device_schema.ionq.ionq_device_capabilities",
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
        "braket.ir.jaqcd.program": {
            "actionType": "braket.ir.jaqcd.program",
            "version": ["1"],
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
            "name": "braket.device_schema.gate_model_qpu_paradigm_properties",
            "version": "1",
        },
        "qubitCount": 11,
        "nativeGateSet": ["ccnot", "cy"],
        "connectivity": {"fullyConnected": False, "connectivityGraph": {"1": ["2", "3"]}},
    },
    "deviceParameters": {},
}


openqasm_valid_input = {
    "braketSchemaHeader": {
        "name": "braket.device_schema.ionq.ionq_device_capabilities",
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
        "braket.ir.openqasm.program": {
            "actionType": "braket.ir.openqasm.program",
            "version": ["1"],
            "supportedOperations": ["x", "y"],
            "supportedResultTypes": [
                {
                    "name": "resultType1",
                    "observables": ["observable1"],
                    "minShots": 2,
                    "maxShots": 4,
                },
            ],
            "supportPhysicalQubits": False,
            "supportedPragmas": ["braket_noise_bit_flip"],
            "forbiddenPragmas": ["braket_unitary_matrix"],
            "forbiddenArrayOperations": ["concatenation", "range", "slicing"],
            "requiresAllQubitsMeasurement": False,
            "requiresContiguousQubitIndices": False,
            "supportsPartialVerbatimBox": False,
            "supportsUnassignedMeasurements": False,
        }
    },
    "paradigm": {
        "braketSchemaHeader": {
            "name": "braket.device_schema.gate_model_qpu_paradigm_properties",
            "version": "1",
        },
        "qubitCount": 11,
        "nativeGateSet": ["ccnot", "cy"],
        "connectivity": {"fullyConnected": False, "connectivityGraph": {"1": ["2", "3"]}},
    },
    "deviceParameters": {},
}


@pytest.mark.parametrize("valid_input", [openqasm_valid_input, jaqcd_valid_input])
def test_valid(valid_input):
    result = IonqDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
    assert result.braketSchemaHeader.name == "braket.device_schema.ionq.ionq_device_capabilities"


@pytest.mark.parametrize("valid_input", [openqasm_valid_input, jaqcd_valid_input])
def test_valid_provider(valid_input):
    valid_input = dict(valid_input)
    valid_input["provider"] = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.ionq.ionq_provider_properties",
            "version": "1",
        },
        "fidelity": {"1Q": {"mean": 0.99717}, "2Q": {"mean": 0.9696}, "spam": {"mean": 0.9961}},
        "timing": {
            "T1": 10000000000,
            "T2": 500000,
            "1Q": 1.1e-05,
            "2Q": 0.00021,
            "readout": 0.000175,
            "reset": 3.5e-05,
        },
        "errorMitigation": {Debias: {"minimumShots": 2500}},
    }
    result = IonqDeviceCapabilities.parse_obj(valid_input)
    assert result.braketSchemaHeader.name == "braket.device_schema.ionq.ionq_device_capabilities"
    assert result == IonqDeviceCapabilities.parse_raw(result.json())


def test_valid_standardized():
    valid_input = dict(openqasm_valid_input)

    valid_input["standardized"] = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.standardized_gate_model_qpu_device_properties",
            "version": "3",
        },
        "oneQubitProperties": {
            "0": {
                "oneQubitFidelity": [
                    {
                        "fidelityType": {
                            "name": "RANDOMIZED_BENCHMARKING",
                            "description": "Single qubit randomized benchmarking",
                        },
                        "fidelity": 0.9985,
                        "standardError": 0.0003,
                        "unit": "fraction",
                    }
                ]
            },
            "1": {
                "oneQubitFidelity": [
                    {
                        "fidelityType": {
                            "name": "RANDOMIZED_BENCHMARKING",
                            "description": "Single qubit randomized benchmarking",
                        },
                        "fidelity": 0.9982,
                        "standardError": 0.0004,
                        "unit": "fraction",
                    }
                ]
            },
        },
        "T1": {"value": 50.0, "standardError": 2.5, "unit": "s"},
        "T2": {"value": 30.0, "standardError": 1.5, "unit": "s"},
        "readoutFidelity": [{"fidelity": 0.9950, "standardError": 0.0010, "unit": "fraction"}],
        "readoutDuration": {"value": 0.000350, "standardError": 0.000010, "unit": "s"},
        "singleQubitGateDuration": {"value": 0.000020, "standardError": 0.000002, "unit": "s"},
        "twoQubitGateFidelity": [
            {
                "fidelityType": {
                    "name": "RANDOMIZED_BENCHMARKING",
                    "description": "Two qubit randomized benchmarking",
                },
                "fidelity": 0.9950,
                "standardError": 0.0010,
                "unit": "fraction",
            }
        ],
        "twoQubitGateDuration": {"value": 0.000200, "standardError": 0.000010, "unit": "s"},
        "updatedAt": "2025-02-22T12:29:03Z",
    }
    IonqDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.parametrize("valid_input", [openqasm_valid_input, jaqcd_valid_input])
@pytest.mark.xfail(raises=ValidationError)
def test__missing_schemaHeader(valid_input):
    valid_input.pop("braketSchemaHeader")
    IonqDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.parametrize("valid_input", [openqasm_valid_input, jaqcd_valid_input])
@pytest.mark.xfail(raises=ValidationError)
def test_missing_paradigm(valid_input):
    valid_input.pop("paradigm")
    IonqDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.parametrize("valid_input", [openqasm_valid_input, jaqcd_valid_input])
@pytest.mark.xfail(raises=ValidationError)
def test_missing_deviceParameters(valid_input):
    valid_input.pop("deviceParameters")
    IonqDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.parametrize("valid_input", [openqasm_valid_input, jaqcd_valid_input])
@pytest.mark.xfail(raises=ValidationError)
def test_missing_action(valid_input):
    valid_input.pop("action")
    IonqDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.parametrize("valid_input", [openqasm_valid_input, jaqcd_valid_input])
@pytest.mark.xfail(raises=ValidationError)
def test_missing_service(valid_input):
    valid_input.pop("service")
    IonqDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
