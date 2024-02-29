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
import math

import pytest
from pydantic.v1 import ValidationError

from braket.device_schema.quera import QueraDeviceCapabilities


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.quera.quera_device_capabilities",
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
                    "windowStartHour": "09:00",
                    "windowEndHour": "10:00",
                }
            ],
            "shotsRange": [1, 10000],
            "deviceCost": {"price": 0.25, "unit": "minute"},
            "deviceDocumentation": {
                "imageUrl": "image_url",
                "summary": "Summary on the device",
                "externalDocumentationUrl": "external doc link",
            },
            "deviceLocation": "us-east-1",
            "updatedAt": "2022-04-16T19:28:02.869136",
        },
        "action": {
            "braket.ir.ahs.program": {
                "actionType": "braket.ir.ahs.program",
                "version": ["1"],
            }
        },
        "deviceParameters": "",
        "paradigm": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.quera.quera_ahs_paradigm_properties",
                "version": "1",
            },
            "qubitCount": 256,
            "lattice": {
                "area": {
                    "width": 100.0e-6,
                    "height": 100.0e-6,
                },
                "geometry": {
                    "spacingRadialMin": 4.0e-6,
                    "spacingVerticalMin": 2.5e-6,
                    "positionResolution": 1e-7,
                    "numberSitesMax": 256,
                },
            },
            "rydberg": {
                "c6Coefficient": 2 * math.pi * 862690,
                "rydbergGlobal": {
                    "rabiFrequencyRange": [0, 2 * math.pi * 4.0e6],
                    "rabiFrequencyResolution": 400,
                    "rabiFrequencySlewRateMax": 2 * math.pi * 4e6 / 100e-9,
                    "detuningRange": [-2 * math.pi * 20.0e6, 2 * math.pi * 20.0e6],
                    "detuningResolution": 0.2,
                    "detuningSlewRateMax": 2 * math.pi * 40.0e6 / 100e-9,
                    "phaseRange": [-99, 99],
                    "phaseResolution": 5e-7,
                    "phaseSlewRateMax": 2 * math.pi / 100e-9,
                    "timeResolution": 1e-9,
                    "timeDeltaMin": 1e-8,
                    "timeMin": 0,
                    "timeMax": 4.0e-6,
                },
                "rydbergLocal": {
                    "detuningRange": [0, 2 * math.pi * 50.0e6],
                    "commonDetuningResolution": 2000,
                    "localDetuningResolution": 0.01,
                    "detuningSlewRateMax": 1 / 100e-9,
                    "numberLocalDetuningSites": 256,
                    "spacingRadialMin": 5e-6,
                    "timeResolution": 1e-9,
                    "timeDeltaMin": 1e-8,
                },
            },
            "performance": {
                "lattice": {
                    "positionErrorAbs": 0.025e-6,
                    "sitePositionError": 0.025e-6,
                    "atomPositionError": 0.025e-6,
                    "fillingErrorTypical": 0.005,
                    "fillingErrorWorst": 0.01,
                    "vacancyErrorTypical": 0.005,
                    "vacancyErrorWorst": 0.005,
                    "atomLossProbabilityTypical": 0.01,
                    "atomLossProbabilityWorst": 0.01,
                    "atomCaptureProbabilityTypical": 0.01,
                    "atomCaptureProbabilityWorst": 0.01,
                    "atomDetectionErrorFalsePositiveTypical": 0.01,
                    "atomDetectionErrorFalsePositiveWorst": 0.01,
                    "atomDetectionErrorFalseNegativeTypical": 0.01,
                    "atomDetectionErrorFalseNegativeWorst": 0.01,
                },
                "rydberg": {
                    "rydbergGlobal": {
                        "rabiFrequencyErrorRel": 0.01,
                        "rabiFrequencyHomogeneityRel": 0.05,
                        "rabiFrequencyHomogeneityAbs": 60e3,
                        "detuningErrorAbs": 2 * math.pi * 10.0e3,
                        "phaseErrorAbs": 2 * math.pi / 1000,
                        "omegaTau": 10,
                        "singleQubitFidelity": 0.95,
                        "twoQubitFidelity": 0.95,
                        "rabiFrequencyGlobalErrorRel": 0.01,
                        "rabiFrequencyInhomogeneityRel": 0.01,
                        "groundDetectionError": 0.01,
                        "rydbergDetectionError": 0.1,
                        "groundPrepError": 0.01,
                        "rydbergPrepErrorBest": 0.05,
                        "rydbergPrepErrorWorst": 0.05,
                        "T1Single": 100e-6,
                        "T1Ensemble": 100e-6,
                        "T2StarSingle": 5e-6,
                        "T2StarEnsemble": 5e-6,
                        "T2EchoSingle": 5e-6,
                        "T2EchoEnsemble": 5e-6,
                        "T2RabiSingle": 5e-6,
                        "T2RabiEnsemble": 5e-6,
                        "T2BlockadedRabiSingle": 5e-6,
                        "T2BlockadedRabiEnsemble": 5e-6,
                        "detuningError": 1e6,
                        "detuningInhomogeneity": 1e6,
                        "rabiAmplitudeRampCorrection": [
                            {
                                "rampTime": 50e-9,
                                "rabiCorrection": 0.92,
                            },
                            {"rampTime": 75e-9, "rabiCorrection": 0.97},
                            {"rampTime": 100e-9, "rabiCorrection": 1.00},
                        ],
                    },
                    "rydbergLocal": {
                        "detuningDynamicRange": 10,
                        "detuningErrorRel": 0.01,
                        "detuningHomogeneity": 0.02,
                        "detuningScaleErrorRel": 0.01,
                        "darkErrorRete": 1e3,
                        "brightErrorRate": 3e6,
                    },
                },
                "detection": {
                    "atomDetectionFidelity": 0.99,
                    "vacancyDetectionFidelity": 0.999,
                    "groundStateDetectionFidelity": 0.99,
                    "rydbergStateDetectionFidelity": 0.99,
                },
                "sorting": {
                    "moveFidelity": 0.98,
                    "patternFidelitySquare": 1e-4,
                },
            },
        },
    }
    return input


def test_valid(valid_input):
    result = QueraDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
    assert result.braketSchemaHeader.name == "braket.device_schema.quera.quera_device_capabilities"


@pytest.mark.xfail(raises=ValidationError)
def test__missing_schemaHeader(valid_input):
    valid_input.pop("braketSchemaHeader")
    QueraDeviceCapabilities.parse_raw_schema(json.dumps(valid_input))
