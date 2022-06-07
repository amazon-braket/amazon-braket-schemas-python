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

from decimal import Decimal
from typing import List

from pydantic import BaseModel, Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class Area(BaseModel):
    """
    The area of the FOV
    Attributes:
        width (Decimal): The width of the FOV accessible
        height (Decimal): The height of the FOV accessible
    """

    width: Decimal
    height: Decimal


class Geometry(BaseModel):
    """
    Spacing or number of sites or rows
    Attributes:
        spacingRadialMin (Decimal): Minimum radial spacing between any two sites in the lattice
        spacingVerticalMin (Decimal): Minimum spacing between any two rows in the lattice
        positionResolution (Decimal): Resolution with which site positions can be specified
        numberSitesMax (int): Maximum number of sites that can be placed in the lattice
    """

    spacingRadialMin: Decimal
    spacingVerticalMin: Decimal
    positionResolution: Decimal
    numberSitesMax: int


class Lattice(BaseModel):
    """
    Spacing or number of sites or rows
    Attributes:
        area : Minimum radial spacing between any two sites
        geometry : Minimum spacing between any two rows
    """

    area: Area
    geometry: Geometry


class RydbergGlobal(BaseModel):
    """
    Rydberg Global
    Attributes:
        rabiFrequencyRange (List[Decimal]): Achievable Rabi frequency range
            for the global Rydberg drive waveform
        rabiFrequencyResolution (Decimal): Resolution with which global Rabi
            frequency amplitude can be specified
        rabiFrequencySlewRateMax (Decimal): Maximum slew rate for changing the
            global Rabi frequency
        detuningRange(List[Decimal]): Achievable detuning range for the global
            Rydberg pulse
        detuningResolution(Decimal): Resolution with which global detuning
            can be specified
        detuningSlewRateMax (Decimal): Maximum slew rate for detuning
        phaseRange(List[Decimal]): Achievable phase range for the global
            Rydberg pulse
        phaseResolution(Decimal): Resolution with which global Rabi frequency
            phase can be specified
        phaseSlewRateMax(Decimal): Maximum slew rate for phase
        timeResolution(Decimal): Resolution with which times for global
            Rydberg drive parameters can be specified
        timeDeltaMin(Decimal): Minimum time step with which times for
            global Rydberg drive parameters can be specified
    """

    rabiFrequencyRange: List[Decimal]
    rabiFrequencyResolution: Decimal
    rabiFrequencySlewRateMax: Decimal
    detuningRange: List[Decimal]
    detuningResolution: Decimal
    detuningSlewRateMax: Decimal
    phaseRange: List[Decimal]
    phaseResolution: Decimal
    phaseSlewRateMax: Decimal
    timeResolution: Decimal
    timeDeltaMin: Decimal


class RydbergLocal(BaseModel):
    """
    Rydberg Local
    Attributes:
        detuningRange (List[Decimal]): Achievable detuning range for
            local detuning patterns
        commonDetuningResolution(Decimal): Resolution with which time-dependent
            term of local detuning can be specified
        localDetuningResolution(Decimal): Resolution with which site-dependent
            coefficients can be specified
        detuningSlewRateMax(Decimal): Maximum slew rate for changing the local detuning
        numberLocalDetuningSites (int): Max number of sites available for the
            local Rydberg detuning pattern
        spacingRadialMin (Decimal): Minimum radial spacing between any two
            sites in the local detuning pattern
        timeResolution(Decimal): Resolution with which times for local Rydberg
            drive parameters can be specified
        timeDeltaMin(Decimal): Minimum time step with which times for local
            Rydberg drive parameters can be specified
    """

    detuningRange: List[Decimal]
    commonDetuningResolution: Decimal
    localDetuningResolution: Decimal
    detuningSlewRateMax: Decimal
    numberLocalDetuningSites: int
    spacingRadialMin: Decimal
    timeResolution: Decimal
    timeDeltaMin: Decimal


class Rydberg(BaseModel):
    """
    Rydberg Model
    Attributes:
        c6Coefficient (Decimal): Rydberg-Rydberg C6 interaction coefficient
        timeMax (Decimal): Maximum duration of Rydberg drive
        rydbergGlobal: Rydberg Global
        rydbergLocal: Rydberg Local
    """

    c6Coefficient: Decimal
    timeMax: Decimal
    rydbergGlobal: RydbergGlobal
    rydbergLocal: RydbergLocal


class PerformanceRydbergGeometry(BaseModel):
    """
    Performance of Rydberg Geometry
    Attributes:
        positionErrorAbs (Decimal): Error between target and actual site position
    """

    positionErrorAbs: Decimal


class PerformanceRydbergGlobal(BaseModel):
    """
    Performance of Rydberg Global
    Attributes:
        rabiFrequencyErrorRel (Decimal): random error in the Rabi frequency, relative
        rabiFrequencyHomogeneity (Decimal): fractional RMS Rabi frequency
            non-uniformity across the user area
        detuningErrorAbs (Decimal): random error in the detuning, absolute
        phaseErrorAbs (Decimal): random error in the phase, absolute
        omegaTau (Decimal): Product of Rabi frequency and Rabi decay time
            for a single qubit under resonant Rydberg drive - average over
            field of view (no local detuning applied)
        singleQubitFidelity (Decimal): Single qubit fidelity of a pi(3.14)  pulse
        twoQubitFidelity (Decimal): Fidelity of two-qubit entangled state
    """

    rabiFrequencyErrorRel: Decimal
    rabiFrequencyHomogeneity: Decimal
    detuningErrorAbs: Decimal
    phaseErrorAbs: Decimal
    omegaTau: Decimal
    singleQubitFidelity: Decimal
    twoQubitFidelity: Decimal


class PerformanceRydbergLocal(BaseModel):
    """
    Performance of Rydberg Local
    Attributes:
        detuningDynamicRange (Decimal): Dynamic range over which the
            specified local detuning accuracy is preserved, relative to max detuning used.
            E.g. if the largest local detuning is 2*pi(3.14) *37.0e6 rad/s, detuning
            accuracy (error) is preserved for other sites down to 2*pi(3.14) *3.7e6
        detuningErrorRel (Decimal):random local detuning error, relative to the given local detuning
        detuningHomogeneity (Decimal): worst-case fractional RMS detuning non-uniformity of
            the detuning pattern, relative to the max detuning used in the detuning pattern;
            applies over the specified dynamic range only
        detuningScaleErrorRel (Decimal): Error on the global scaling factor for local
            detuning, relative
        darkErrorRete (Decimal): Error rate induced by local detuning pattern under Rydberg
            drive for qubits maximally detuned by the local detuning pattern (scattering)
    """

    detuningDynamicRange: Decimal
    detuningErrorRel: Decimal
    detuningHomogeneity: Decimal
    detuningScaleErrorRel: int
    darkErrorRete: Decimal


class PerformanceRydberg(BaseModel):
    """
    Rydberg Performance
    Attributes:
        geometry : Performance of Rydberg Geometry
        global: Performance of Rydberg Global
        local: Performance of Rydberg Local
    """

    geometry: PerformanceRydbergGeometry
    global_rydberg: PerformanceRydbergGlobal = Field(None, alias="global")
    local: PerformanceRydbergLocal


class Detection(BaseModel):
    """
    Detection of an atom
    Attributes:
        atomDetectionFidelity (Decimal): Probability to correctly detect the presence of an atom
        vacancyDetectionFidelity (Decimal): Probability to correctly detect the absence of an atom
    """

    atomDetectionFidelity: Decimal
    vacancyDetectionFidelity: Decimal


class Sorting(BaseModel):
    """
    Probability for sorting or arranging
    Attributes:
        moveFidelity (Decimal): Probability for a single sorting move to succeed
        patternFidelitySquare (Decimal): Probability of successfully arranging a maximal square
            pattern (256 qubits, filling field of view)
    """

    moveFidelity: Decimal
    patternFidelitySquare: Decimal


class Performance(BaseModel):
    """
    Performance
    Attributes:
        rydberg : Rydberg Performance
        detection : Detection of an atom
        sorting : Probability for sorting or arranging
    """

    rydberg: PerformanceRydberg
    detection: Detection
    sorting: Sorting


class QueraAhsParadigmProperties(BraketSchemaBase):
    """
    This defines the properties common to ahs Quera devices.

    Attributes:
        area: the area of the FOV
        geometry: spacing or number of sites or rows
        qubits: the number of qubits
        rydberg: the constraint of rydberg
        performance: the performance of rydberg or atom detection
    Examples:
        >>> import json
        >>> input_json = {
        ...     "braketSchemaHeader": {
        ...         "name": "braket.device_schema.quera.quera_ahs_paradigm_properties",
        ...         "version": "1",
        ...     },
        ...     "qubitCount": 256,
        ...     "lattice":{
        ...         "area": {
        ...             "width": 100.0e-6,
        ...             "height": 100.0e-6,
        ...         },
        ...         "geometry": {
        ...             "spacingRadialMin": 4.0e-6,
        ...             "spacingVerticalMin": 2.5e-6,
        ...             "positionResolution": 1e-7,
        ...             "numberSitesMax": 256,
        ...         }
        ...     },
        ...     "rydberg": {
        ...         "c6Coefficient": 2*math.pi(3.14) *862690,
        ...         "timeMax": 4.0e-6,
        ...         "rydbergGlobal": {
        ...             "rabiFrequencyRange": [0, 2*math.pi(3.14) *4.0e6],
        ...             "rabiFrequencyResolution": 400
        ...             "rabiFrequencySlewRateMax": 2*math.pi(3.14) *4e6/100e-9,
        ...             "detuningRange": [-2*math.pi(3.14) *20.0e6,2*math.pi(3.14) *20.0e6],
        ...             "detuningResolution": 0.2,
        ...             "detuningSlewRateMax": 2*math.pi(3.14) *40.0e6/100e-9,
        ...             "phaseRange": [-99,99],
        ...             "phaseResolution": 5e-7,
        ...             "phaseSlewRateMax": 2*math.pi(3.14) /100e-9,
        ...             "timeResolution": 1e-9,
        ...             "timeDeltaMin": 1e-8,
        ...         },
        ...         "rydbergLocal": {
        ...             "detuningRange": [0,2*math.pi(3.14) *50.0e6],
        ...             "commonDetuningResolution": 2000,
        ...             "localDetuningResolution": 0.01,
        ...             "detuningSlewRateMax": 1/100e-9,
        ...             "numberLocalDetuningSites": 256,
        ...             "spacingRadialMin": 5e-6,
        ...             "timeResolution": 1e-9,
        ...             "timeDeltaMin": 1e-8,
        ...         },
        ...     },
        ... }
        >>> QueraAhsParadigmProperties.parse_raw_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.quera.quera_ahs_paradigm_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    qubitCount: int
    lattice: Lattice
    rydberg: Rydberg
