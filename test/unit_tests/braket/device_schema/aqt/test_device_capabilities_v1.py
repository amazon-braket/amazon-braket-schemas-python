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
from braket.schema_common import BraketSchemaBase
from braket.device_schema.aqt.aqt_device_capabilities_v1 import AqtDeviceCapabilities


def test_schema_parse_obj():
    input = {
        "action": {
            "braket.ir.openqasm.program": {
                "version": ["1.0"],
                "actionType": "braket.ir.openqasm.program",
                "supportedOperations": [
                    "ccnot",
                    "cnot",
                    "cphaseshift",
                    "cphaseshift00",
                    "cphaseshift01",
                    "cphaseshift10",
                    "cswap",
                    "swap",
                    "iswap",
                    "pswap",
                    "ecr",
                    "cy",
                    "cz",
                    "xy",
                    "xx",
                    "yy",
                    "zz",
                    "h",
                    "i",
                    "phaseshift",
                    "rx",
                    "ry",
                    "rz",
                    "s",
                    "si",
                    "t",
                    "ti",
                    "v",
                    "vi",
                    "x",
                    "y",
                    "z",
                    "prx",
                ],
                "supportedModifiers": [],
                "supportedPragmas": [
                    "verbatim",
                    "braket_result_type_sample",
                    "braket_result_type_expectation",
                    "braket_result_type_variance",
                    "braket_result_type_probability",
                ],
                "forbiddenPragmas": [
                    "braket_unitary_matrix",
                    "braket_result_type_state_vector",
                    "braket_result_type_density_matrix",
                    "braket_result_type_amplitude",
                ],
                "maximumQubitArrays": 1,
                "maximumClassicalArrays": 1,
                "forbiddenArrayOperations": [
                    "concatenation",
                    "negativeIndex",
                    "range",
                    "rangeWithStep",
                    "slicing",
                    "selection",
                ],
                "requiresAllQubitsMeasurement": False,
                "supportPhysicalQubits": True,
                "requiresContiguousQubitIndices": False,
                "supportsPartialVerbatimBox": True,
                "supportsUnassignedMeasurements": False,
                "disabledQubitRewiringSupported": False,
                "supportedResultTypes": [
                    {
                        "name": "Sample",
                        "observables": ["x", "y", "z", "h", "i"],
                        "minShots": 1,
                        "maxShots": 20000,
                    },
                    {
                        "name": "Expectation",
                        "observables": ["x", "y", "z", "h", "i"],
                        "minShots": 1,
                        "maxShots": 20000,
                    },
                    {
                        "name": "Variance",
                        "observables": ["x", "y", "z", "h", "i"],
                        "minShots": 1,
                        "maxShots": 20000,
                    },
                    {"name": "Probability", "minShots": 1, "maxShots": 20000},
                ],
            }
        },
        "braketSchemaHeader": {
            "name": "braket.device_schema.aqt.aqt_device_capabilities",
            "version": "1",
        },
        "deviceParameters": {
            "definitions": {
                "GateModelParameters": {
                    "description": 'Defines parameters common to all gate model devices.\n\nAttributes:\n    qubitCount: Number of qubits used by the circuit.\n    disableQubitRewiring: Whether to run the circuit with the exact qubits chosen,\n        without any rewiring downstream.\n        If ``True``, no qubit rewiring is allowed; if ``False``, qubit rewiring is allowed.\n\nExamples:\n    >>> import json\n    >>> input_json = {\n    ...    "braketSchemaHeader": {\n    ...        "name": "braket.device_schema.gate_model_parameters",\n    ...        "version": "1"\n    ...    },\n    ...    "qubitCount": 1,\n    ...    "disableQubitRewiring": true\n    ... }\n    >>> GateModelParameters.parse_raw_schema(json.dumps(input_json))',
                    "properties": {
                        "braketSchemaHeader": {
                            "const": {
                                "name": "braket.device_schema.gate_model_parameters",
                                "version": "1",
                            },
                            "default": {
                                "name": "braket.device_schema.gate_model_parameters",
                                "version": "1",
                            },
                            "title": "Braketschemaheader",
                        },
                        "disableQubitRewiring": {
                            "default": False,
                            "title": "Disablequbitrewiring",
                            "type": "boolean",
                        },
                        "qubitCount": {"minimum": 0, "title": "Qubitcount", "type": "integer"},
                    },
                    "required": ["qubitCount"],
                    "title": "GateModelParameters",
                    "type": "object",
                }
            },
            "description": "Schema for parameters shared across all gate model devices.\n\nArgs:\n    braketSchemaHeader (BraketSchemaHeader): Schema header containing name and version.\n    paradigmParameters (GateModelParameters): Parameters specific to gate model devices.",
            "properties": {
                "braketSchemaHeader": {
                    "const": {
                        "name": "braket.device_schema.common.gate_model_device_parameters",
                        "version": "1",
                    },
                    "default": {
                        "name": "braket.device_schema.common.gate_model_device_parameters",
                        "version": "1",
                    },
                    "title": "Braketschemaheader",
                },
                "paradigmParameters": {"$ref": "#/definitions/GateModelParameters"},
            },
            "required": ["paradigmParameters"],
            "title": "GateModelDeviceParameters",
            "type": "object",
        },
        "paradigm": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.gate_model_qpu_paradigm_properties",
                "version": "1",
            },
            "connectivity": {"connectivityGraph": {}, "fullyConnected": True},
            "nativeGateSet": ["r", "rxx", "rz"],
            "qubitCount": 12,
        },
        "provider": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.aqt.aqt_provider_properties",
                "version": "1",
            },
            "properties": {
                "readout_time_micros": 1500,
                "mean_two_qubit_gate_fidelity": {"uncertainty": 0.0019, "value": 98.9},
                "single_qubit_gate_fidelity": {
                    "0": {"uncertainty": 0.00002, "value": 99.9998},
                    "1": {"uncertainty": 0.00003, "value": 99.99972},
                    "2": {"uncertainty": 0.00007, "value": 99.99941},
                    "3": {"uncertainty": 0.00004, "value": 99.99969},
                    "4": {"uncertainty": 0.00003, "value": 99.99973},
                    "5": {"uncertainty": 0.00002, "value": 99.9998},
                    "6": {"uncertainty": 0.00004, "value": 99.99952},
                    "7": {"uncertainty": 0.00007, "value": 99.99956},
                    "8": {"uncertainty": 0.00003, "value": 99.99962},
                    "9": {"uncertainty": 0.00002, "value": 99.99979},
                    "10": {"uncertainty": 0.00008, "value": 99.99932},
                    "11": {"uncertainty": 0.00002, "value": 99.99978},
                },
                "single_qubit_gate_duration_micros": 22,
                "spam_fidelity_lower_bound": 99.74,
                "t1_s": {"uncertainty": 0.007, "value": 1.168},
                "t2_coherence_time_s": {"uncertainty": 31.3, "value": 173.8},
                "two_qubit_gate_duration_micros": 660,
                "updated_at": "2025-03-28T12:29:03",
            },
        },
        "service": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.device_service_properties",
                "version": "1",
            },
            "deviceCost": {"price": 0.00145, "unit": "shot"},
            "deviceDocumentation": {
                "externalDocumentationUrl": "https://www.aqt.eu/products/ibex-q1/",
                "imageUrl": "",
                "summary": "TODO",
            },
            "deviceLocation": "Innsbruck, Austria",
            "executionWindows": [
                {"executionDay": "TODO", "windowEndHour": "10:00:00", "windowStartHour": "08:00:00"}
            ],
            "shotsRange": [1, 2000],
            "updatedAt": "2025-02-07T17:39:04.646742+00:00",
        },
        "standardized": {
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
            "ReadoutFidelity": [
                {
                    "fidelityType": {
                        "name": "RANDOMIZED_BENCHMARKING",
                        "description": "Readout fidelity measurement",
                    },
                    "fidelity": 0.9950,
                    "standardError": 0.0010,
                    "unit": "fraction",
                }
            ],
            "ReadoutDuration": {"value": 0.000350, "standardError": 0.000010, "unit": "s"},
            "SingleQubitGateDuration": {"value": 0.000020, "standardError": 0.000002, "unit": "s"},
            "TwoQubitGateFidelity": [
                {
                    "fidelityType": {
                        "name": "RANDOMIZED_BENCHMARKING",
                        "description": "Single qubit randomized benchmarking",
                    },
                    "fidelity": 0.9950,
                    "standardError": 0.0010,
                    "unit": "fraction",
                }
            ],
            "TwoQubitGateDuration": {"value": 0.000200, "standardError": 0.000010, "unit": "s"},
        },
    }
    assert BraketSchemaBase.parse_raw_schema(json.dumps(input)) == AqtDeviceCapabilities.parse_obj(
        input
    )
