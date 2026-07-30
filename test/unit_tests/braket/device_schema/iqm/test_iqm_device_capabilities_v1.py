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

from braket.device_schema.iqm.iqm_device_capabilities_v1 import IqmDeviceCapabilities

device_properties_data = {
    "braketSchemaHeader": {
        "name": "braket.device_schema.standardized_gate_model_qpu_device_properties",
        "version": "1",
    },
    "oneQubitProperties": {
        "1": {
            "T1": {"value": 0.00002645537061513506, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.000042520352127649304, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.999235141291427,
                    "standardError": 0.000020319733257680807,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.97665},
            ],
        },
        "2": {
            "T1": {"value": 0.00004694189628294441, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.000014525656595970012, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9980790722115301,
                    "standardError": 0.00008378925641774413,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9872999999999998},
            ],
        },
        "3": {
            "T1": {"value": 0.00003780610530390295, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.000012730062976998262, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9989918196852849,
                    "standardError": 0.000036722036948824336,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.978},
            ],
        },
        "4": {
            "T1": {"value": 0.000014044967646269181, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.000010606459095963345, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9988482312254674,
                    "standardError": 0.0000359332104627192,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9842},
            ],
        },
        "5": {
            "T1": {"value": 0.00005555343969248793, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.000040328164808328, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.998858772628301,
                    "standardError": 0.00003459172244195506,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9624000000000001},
            ],
        },
        "6": {
            "T1": {"value": 0.00004755639869157383, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.0000371462614291675, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9990635125102881,
                    "standardError": 0.000030207241818194626,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9828},
            ],
        },
        "7": {
            "T1": {"value": 0.000040303616256999366, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.0000402773587754054, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9393374758762614,
                    "standardError": 0.014499746578237388,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.85305},
            ],
        },
        "8": {
            "T1": {"value": 0.000029706838398723327, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.0000402773587754054, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9992131884760928,
                    "standardError": 0.000018498832665640375,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9882500000000001},
            ],
        },
        "9": {
            "T1": {"value": 0.00003497074060629076, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.0000402773587754054, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9988227745902349,
                    "standardError": 0.000020636647713687474,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9466499999999999},
            ],
        },
        "10": {
            "T1": {"value": 0.000025578694019978698, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.000019006026304791726, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9992480366563676,
                    "standardError": 0.00003244083548912805,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9529},
            ],
        },
        "11": {
            "T1": {"value": 0.00003109048085647714, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.000007384068205203541, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9990832666979816,
                    "standardError": 0.000020693293951882814,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9689},
            ],
        },
        "12": {
            "T1": {"value": 0.00001839865825870035, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.00002796146699241044, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9994504150416057,
                    "standardError": 0.000011321194551337402,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9661},
            ],
        },
        "13": {
            "T1": {"value": 0.000008347262321795057, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.000014233999513799374, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9987509374099799,
                    "standardError": 0.000031768925922539336,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.97615},
            ],
        },
        "14": {
            "T1": {"value": 0.000022097971582812903, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.00003575364572218674, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9992381908378727,
                    "standardError": 0.000016170755513255113,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9782499999999998},
            ],
        },
        "15": {
            "T1": {"value": 0.000028087494482909037, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.000041217042636258126, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9991848536775308,
                    "standardError": 0.000024399677325984384,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9449},
            ],
        },
        "16": {
            "T1": {"value": 0.000019260498831163986, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.0000034484103835165677, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.999138538494355,
                    "standardError": 0.000028620752690084272,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9678},
            ],
        },
        "17": {
            "T1": {"value": 0.000022838359799548513, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.000029067173274113016, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9991258538956796,
                    "standardError": 0.00004581378352467071,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9754999999999999},
            ],
        },
        "18": {
            "T1": {"value": 0.000051008577660161, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.0000402773587754054, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9983756295293063,
                    "standardError": 0.00007090365859445918,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9745},
            ],
        },
        "19": {
            "T1": {"value": 0.000051008577660161, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.0000402773587754054, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9994475617317424,
                    "standardError": 0.00001696490858480998,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.9819},
            ],
        },
        "20": {
            "T1": {"value": 0.00001916757238906719, "standardError": 1.697799e-6, "unit": "S"},
            "T2": {"value": 0.000020065645767958196, "standardError": 1.697799e-6, "unit": "S"},
            "oneQubitFidelity": [
                {
                    "fidelityType": {"name": "SIMULTANEOUS_RANDOMIZED_BENCHMARKING"},
                    "fidelity": 0.9980790722115301,
                    "standardError": 0.00008378925641774413,
                },
                {"fidelityType": {"name": "READOUT"}, "fidelity": 0.97745},
            ],
        },
    },
    "twoQubitProperties": {
        "1-2": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9776511733031956,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "1-4": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9761518314116017,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "10-11": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9577915690630964,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "10-15": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9631027205530631,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "10-5": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9576501723401776,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "10-9": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9638671111402636,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                }
            ]
        },
        "11-12": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.985695929902228,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "11-16": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9839274195757519,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "11-6": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9476684856994257,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                }
            ]
        },
        "12-17": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9884119118193532,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "12-7": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.7732248295765016,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "13-14": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9805836404966111,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "13-8": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9816471580056283,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "14-15": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9493439865912552,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "14-18": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9774559154051097,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "14-9": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.977273362693027,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "15-16": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9745948732638371,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "15-19": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9693845254778247,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "16-17": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9827517369345585,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "16-20": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.973250556262393,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "18-19": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9851082856308436,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "19-20": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9885684603053977,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "2-5": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9808555160207241,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "3-4": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9798423459087066,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "3-8": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9768328347774287,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "4-5": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9728127962226439,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "4-9": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9737363526707615,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "5-6": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9556100932308558,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "6-7": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.8356416201354127,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
        "8-9": {
            "twoQubitGateFidelity": [
                {
                    "gateName": "cz",
                    "fidelity": 0.9745065192361164,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
                {
                    "gateName": "Two_Qubit_Clifford",
                    "fidelity": 0.9702100020990085,
                    "standardError": 0.0005598328910389112,
                    "fidelityType": {"name": "SIMULTANEOUS_INTERLEAVED_RANDOMIZED_BENCHMARKING"},
                },
            ]
        },
    },
}

openqasm_valid_input = {
    "braketSchemaHeader": {
        "name": "braket.device_schema.iqm.iqm_device_capabilities",
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
        "shotsRange": [1, 20000],
        "deviceCost": {"price": 0.25, "unit": "shot"},
        "deviceDocumentation": {
            "imageUrl": "image_url",
            "summary": "Summary on the device",
            "externalDocumentationUrl": "exter doc link",
        },
        "deviceLocation": "eu-north-1",
        "updatedAt": "2024-04-04T01:10:02.869136",
    },
    "action": {
        "braket.ir.openqasm.program": {
            "actionType": "braket.ir.openqasm.program",
            "version": ["1"],
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
                "start_verbatim_box",
                "end_verbatim_box",
            ],
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
        },
        "braket.ir.openqasm.program_set": {
            "actionType": "braket.ir.openqasm.program_set",
            "version": ["1"],
            "maximumExecutables": 500,
            "maximumTotalShots": 1_000_000,
        },
    },
    "paradigm": {
        "braketSchemaHeader": {
            "name": "braket.device_schema.gate_model_qpu_paradigm_properties",
            "version": "1",
        },
        "qubitCount": 20,
        "nativeGateSet": ["cz", "prx"],
        "connectivity": {
            "fullyConnected": False,
            "connectivityGraph": {
                "1": ["2", "4"],
                "2": ["5"],
                "3": ["4", "8"],
                "4": ["5", "9"],
                "5": ["6"],
                "6": ["7"],
                "8": ["9"],
                "10": ["11", "15", "5", "9"],
                "11": ["12", "16", "6"],
                "12": ["17", "7"],
                "13": ["14", "8"],
                "14": ["15", "18", "9"],
                "15": ["16", "19"],
                "16": ["17", "20"],
                "18": ["19"],
                "19": ["20"],
            },
        },
    },
    "deviceParameters": {},
    "standardized": device_properties_data,
}


@pytest.mark.parametrize("valid_input", [openqasm_valid_input])
def test_valid(valid_input):
    result = IqmDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
    assert result.braketSchemaHeader.name == "braket.device_schema.iqm.iqm_device_capabilities"


@pytest.mark.parametrize(
    "missing_field", ["braketSchemaHeader", "paradigm", "deviceParameters", "action", "service"]
)
@pytest.mark.parametrize("valid_input", [openqasm_valid_input])
def test_missing_paradigm(valid_input, missing_field):
    with pytest.raises(ValidationError):
        valid_input.pop(missing_field)
        IqmDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
