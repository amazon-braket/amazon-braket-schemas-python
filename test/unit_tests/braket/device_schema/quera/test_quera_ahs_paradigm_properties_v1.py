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

from braket.device_schema.quera.quera_ahs_paradigm_properties_v1 import (
    Area,
    Geometry,
    QueraAhsParadigmProperties,
    RydbergGlobal,
)


@pytest.fixture(scope="module")
def valid_input():
    input = {
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
                "timeResolution": 1e-9,
                "timeDeltaMin": 1e-8,
                "timeMin": 0,
                "timeMax": 4.0e-6,
            },
        },
        "performance": {
            "lattice": {
                "positionErrorAbs": 0.025e-6,
            },
            "rydberg": {
                "rydbergGlobal": {
                    "rabiFrequencyErrorRel": 0.01,
                },
            },
        },
    }
    return input


def test_valid(valid_input):
    result = QueraAhsParadigmProperties.parse_raw_schema(json.dumps(valid_input))
    assert (
        result.braketSchemaHeader.name == "braket.device_schema.quera.quera_ahs_paradigm_properties"
    )


@pytest.mark.parametrize("missing_field", ["braketSchemaHeader", "lattice", "rydberg"])
def test_missing_field(valid_input, missing_field):
    with pytest.raises(ValidationError):
        valid_input.pop(missing_field)
        QueraAhsParadigmProperties.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_field_in_area():
    Area(width=100.0e-6)


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_field_in_area():
    Area(width=100.0e-6, height="foo")


@pytest.mark.xfail(raises=ValidationError)
def test_missing_field_in_geometry():
    Geometry(spacingRadiaMin=4.0e-6, spacingVerticalMin=2.5e-6)


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_field_in_geometry():
    Geometry(
        spacingRadiaMin=4.0e-6,
        spacingVerticalMin="foo",
        positionResolution=1e-7,
        numberOfSitesMax=256,
    )


@pytest.mark.xfail(raises=ValidationError)
def test_missing_field_in_detection():
    Area(atomDetectionFidelity=0.99)


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_field_in_detection():
    Area(atomDetectionFidelity=0.99, vacancyDetectionFidelity="foo")


@pytest.mark.xfail(raises=ValidationError)
def test_missing_field_in_sorting():
    Geometry(moveFidelity=0.98)


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_field_in_sorting():
    Geometry(moveFidelity=4.0e-6, patternFidelitySquare="foo")


@pytest.mark.xfail(raises=ValidationError)
def test_missing_field_in_rydbergGlobal():
    RydbergGlobal(
        rabiFrequencyRange=[0, 2 * math.pi * 4.0e6],
        rabiFrequencySlewRateMax=2 * math.pi * 4e6 / 100e-9,
    )


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_field_in_rydbergGlobal():
    RydbergGlobal(
        rabiFrequencyRange=2.0,
        rabiFrequencySlewRateMax=2 * math.pi * 4e6 / 100e-9,
        detuningRange=[-2 * math.pi * 20.0e6, 2 * math.pi * 20.0e6],
        detuningSlewRateMax=2 * math.pi * 40.0e6 / 100e-9,
        phaseRange=[-99, 99],
        phaseSlewRateMax=2 * math.pi / 100e-9,
        timeDiscretization=1e-9,
        timeMax=4.0e-6,
    )


@pytest.mark.xfail(raises=ValidationError)
def test_missing_field_in_perfomanceRydbergGlobal():
    RydbergGlobal(rabiFrequencyErrorRel=0.01, rabiFrequencyHomogeneityRel=0.05)


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_field_in_perfomanceRydbergGlobal():
    RydbergGlobal(
        rabiFrequencyErrorRel=0.01,
        rabiFrequencyHomogeneityRel=0.05,
        rabiFrequencyHomogeneityAbs=60e3,
        detuningErrorAbs=2 * math.pi * 10.0e3,
        phaseErrorAbs=2 * math.pi / 1000,
        phaseRange=99,
        omegaTau=10,
        singleQubitFidelity=0.95,
        twoQubitFidelity=0.95,
    )
