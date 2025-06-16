from braket.device_schema.standardized_gate_model_qpu_device_properties_v3 import StandardizedGateModelQpuDeviceProperties
import json


def test_parse_success():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.standardized_gate_model_qpu_device_properties",
            "version": "3"
        },
        "oneQubitProperties": {
            "0": {
                "oneQubitFidelity": [
                    {
                        "fidelityType": {
                            "name": "RANDOMIZED_BENCHMARKING",
                            "description": "Single qubit randomized benchmarking"
                        },
                        "fidelity": 0.9985,
                        "standardError": 0.0003,
                        "unit": "fraction"
                    }
                ]
            },
            "1": {
                "oneQubitFidelity": [
                    {
                        "fidelityType": {
                            "name": "RANDOMIZED_BENCHMARKING",
                            "description": "Single qubit randomized benchmarking"
                        },
                        "fidelity": 0.9982,
                        "standardError": 0.0004,
                        "unit": "fraction"
                    }
                ]
            }
        },
        "T1": {
            "value": 50.0,
            "standardError": 2.5,
            "unit": "s"
        },
        "T2": {
            "value": 30.0,
            "standardError": 1.5,
            "unit": "s"
        },
        "readoutFidelity": [{
            "fidelityType": {
                "name": "RANDOMIZED_BENCHMARKING",
                "description": "Readout fidelity measurement"
            },
            "fidelity": 0.9950,
            "standardError": 0.0010,
            "unit": "fraction"
        }],
        "readoutDuration": {
            "value": 0.000350,
            "standardError": 0.000010,
            "unit": "s"
        },
        "singleQubitGateDuration": {
            "value": 0.000020,
            "standardError": 0.000002,
            "unit": "s"
        },
        "oneQubitGateFidelity": [{
                 "fidelityType": {
                     "name": "RANDOMIZED_BENCHMARKING",
                     "description": "Two qubit randomized benchmarking"
                 },
                "fidelity": 0.9950,
                "standardError": 0.0010,
                "unit": "fraction"
        }],
        "twoQubitGateFidelity": [{
                 "fidelityType": {
                     "name": "RANDOMIZED_BENCHMARKING",
                     "description": "Single qubit randomized benchmarking"
                 },
                "fidelity": 0.9950,
                "standardError": 0.0010,
                "unit": "fraction"
        }],
        "twoQubitGateDuration": {
            "value": 0.000200,
            "standardError": 0.000010,
            "unit": "s"
        },
        "updatedAt": "2025-02-22T12:29:03Z"
    }
    assert StandardizedGateModelQpuDeviceProperties.parse_raw_schema(json.dumps(input))
    for key in input.keys() :
        if key not in {"braketSchemaHeader"}:
            copy = input.copy()
            copy.pop(key)
            assert StandardizedGateModelQpuDeviceProperties.parse_raw_schema(json.dumps(copy))
