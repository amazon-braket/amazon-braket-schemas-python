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

from braket.device_schema.oqc.oqc_device_capabilities_v1 import OqcDeviceCapabilities

device_properties_data = {
    "braketSchemaHeader": {
        "name": "braket.device_schema.standardized_gate_model_qpu_device_properties",
        "version": "1",
    },
    "oneQubitProperties": {
        "0": {
            "T1": {"value": 28.9, "standardError": 0.01, "unit": "us"},
            "T2": {"value": 44.5, "standardError": 0.02, "unit": "us"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "READOUT"},
                    "fidelity": 0.9993,
                    "standardError": None,
                },
                {
                    "fidelityType": {"name": "RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.903,
                    "standardError": None,
                },
            ],
        }
    },
    "twoQubitProperties": {
        "0-1": {
            "twoQubitGateFidelity": [
                {
                    "direction": {"control": 0, "target": 1},
                    "gateName": "CNOT",
                    "fidelity": 0.877,
                    "fidelityType": {"name": "INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                }
            ]
        }
    },
}

jaqcd_valid_input = {
    "braketSchemaHeader": {
        "name": "braket.device_schema.oqc.oqc_device_capabilities",
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
        "deviceLocation": "eu-west-2",
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
        "qubitCount": 32,
        "nativeGateSet": ["ccnot", "cy"],
        "connectivity": {"fullyConnected": False, "connectivityGraph": {"1": ["2", "3"]}},
    },
    "deviceParameters": {},
}

openqasm_valid_input = {
    "braketSchemaHeader": {
        "name": "braket.device_schema.oqc.oqc_device_capabilities",
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
            "requireAllQubitsMeasurement": False,
            "requireContiguousQubitIndices": False,
            "supportsPartialVerbatimBox": False,
            "supportsUnassignedMeasurements": False,
        }
    },
    "paradigm": {
        "braketSchemaHeader": {
            "name": "braket.device_schema.gate_model_qpu_paradigm_properties",
            "version": "1",
        },
        "qubitCount": 32,
        "nativeGateSet": ["ccnot", "cy"],
        "connectivity": {"fullyConnected": False, "connectivityGraph": {"1": ["2", "3"]}},
    },
    "deviceParameters": {},
    "standardized": device_properties_data,
}


@pytest.mark.parametrize("valid_input", [openqasm_valid_input, jaqcd_valid_input])
def test_valid(valid_input):
    result = OqcDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
    assert result.braketSchemaHeader.name == "braket.device_schema.oqc.oqc_device_capabilities"


@pytest.mark.parametrize(
    "missing_field", ["braketSchemaHeader", "paradigm", "deviceParameters", "action", "service"]
)
@pytest.mark.parametrize("valid_input", [openqasm_valid_input, jaqcd_valid_input])
def test_missing_paradigm(valid_input, missing_field):
    with pytest.raises(ValidationError):
        valid_input.pop(missing_field)
        OqcDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
