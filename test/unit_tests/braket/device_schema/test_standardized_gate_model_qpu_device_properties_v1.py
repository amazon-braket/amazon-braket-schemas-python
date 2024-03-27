import json

import pytest
from pydantic.v1 import ValidationError

from braket.device_schema.standardized_gate_model_qpu_device_properties_v1 import (
    StandardizedGateModelQpuDeviceProperties,
)


@pytest.fixture(scope="module")
def valid_input():
    input = {
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
                        "fidelityType": {
                            "name": "RANDOMIZED_BENCHMARKING",
                            "description": "uses a standard RB technique",
                        },
                        "fidelity": 0.9993,
                    },
                    {
                        "fidelityType": {"name": "READOUT"},
                        "fidelity": 0.903,
                        "standardError": None,
                    },
                ],
            },
            "1": {
                "T1": {"value": 28.9, "unit": "us"},
                "T2": {"value": 44.5, "standardError": 0.02, "unit": "us"},
                "oneQubitFidelity": [
                    {
                        "fidelityType": {"name": "RANDOMIZED_BENCHMARKING"},
                        "fidelity": 0.9986,
                        "standardError": None,
                    },
                    {
                        "fidelityType": {"name": "READOUT"},
                        "fidelity": 0.867,
                        "standardError": None,
                    },
                ],
            },
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
            },
            "0-7": {
                "twoQubitGateFidelity": [
                    {
                        "direction": {"control": 0, "target": 7},
                        "gateName": "CNOT",
                        "fidelity": 0.877,
                        "standardError": 0.001,
                        "fidelityType": {"name": "INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                    }
                ]
            },
        },
    }
    return input


def test_valid(valid_input):
    result = StandardizedGateModelQpuDeviceProperties.parse_raw_schema(json.dumps(valid_input))
    assert (
        result.braketSchemaHeader.name
        == "braket.device_schema.standardized_gate_model_qpu_device_properties"
    )


@pytest.mark.parametrize(
    "missing_field", ["braketSchemaHeader", "oneQubitProperties", "twoQubitProperties"]
)
def test_missing_field(valid_input, missing_field):
    with pytest.raises(ValidationError):
        valid_input.pop(missing_field)
        StandardizedGateModelQpuDeviceProperties.parse_raw_schema(json.dumps(valid_input))
