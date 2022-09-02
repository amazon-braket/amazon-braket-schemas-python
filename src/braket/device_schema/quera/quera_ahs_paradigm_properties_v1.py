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
from typing import Tuple

from pydantic import BaseModel, Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class Area(BaseModel):
    """
    The area of the FOV
    Attributes:
        width (Decimal): Largest allowed difference between x
            coordinates of any two sites (measured in meters)
        height (Decimal): Largest allowed difference between y
            coordinates of any two sites (measured in meters)
    """

    width: Decimal
    height: Decimal


class Geometry(BaseModel):
    """
    Spacing or number of sites or rows
    Attributes:
        spacingRadialMin (Decimal): Minimum radial spacing between any
            two sites in the lattice (measured in meters)
        spacingVerticalMin (Decimal): Minimum spacing between any two
            rows in the lattice (measured in meters)
        positionResolution (Decimal): Resolution with which site positions
            can be specified (measured in meters)
        numberSitesMax (int): Maximum number of sites that can be placed
            in the lattice
    """

    spacingRadialMin: Decimal
    spacingVerticalMin: Decimal
    positionResolution: Decimal
    numberSitesMax: int


class Lattice(BaseModel):
    """
    Spacing or number of sites or rows
    Attributes:
        area : The rectangular area available for arranging atomic sites
        geometry : Limitations of atomic site arrangements
    """

    area: Area
    geometry: Geometry


class RydbergGlobal(BaseModel):
    """
    Parameters determining the limitations on the driving field that drives the
        ground-to-Rydberg transition uniformly on all atoms
    Attributes:
        rabiFrequencyRange (Tuple[Decimal,Decimal]): Achievable Rabi frequency
            range for the global Rydberg drive waveform (measured in rad/s)
        rabiFrequencyResolution (Decimal): Resolution with which global Rabi
            frequency amplitude can be specified (measured in rad/s)
        rabiFrequencySlewRateMax (Decimal): Maximum slew rate for changing the
            global Rabi frequency (measured in (rad/s)/s)
        detuningRange(Tuple[Decimal,Decimal]): Achievable detuning range for
            the global Rydberg pulse (measured in rad/s)
        detuningResolution(Decimal): Resolution with which global detuning can
            be specified (measured in rad/s)
        detuningSlewRateMax (Decimal): Maximum slew rate for detuning (measured in (rad/s)/s)
        phaseRange(Tuple[Decimal,Decimal]): Achievable phase range for the global
            Rydberg pulse (measured in rad)
        phaseResolution(Decimal): Resolution with which global Rabi frequency phase
            can be specified (measured in rad)
        phaseSlewRateMax(Decimal): Maximum slew rate for phase (measured in rad/s)
        timeResolution(Decimal): Resolution with which times for global Rydberg drive
            parameters can be specified (measured in s)
        timeDeltaMin(Decimal): Minimum time step with which times for global Rydberg
            drive parameters can be specified (measured in s)
        timeMin (Decimal): Minimum duration of Rydberg drive (measured in s)
        timeMax (Decimal): Maximum duration of Rydberg drive (measured in s)
    """

    rabiFrequencyRange: Tuple[Decimal, Decimal]
    rabiFrequencyResolution: Decimal
    rabiFrequencySlewRateMax: Decimal
    detuningRange: Tuple[Decimal, Decimal]
    detuningResolution: Decimal
    detuningSlewRateMax: Decimal
    phaseRange: Tuple[Decimal, Decimal]
    phaseResolution: Decimal
    phaseSlewRateMax: Decimal
    timeResolution: Decimal
    timeDeltaMin: Decimal
    timeMin: Decimal
    timeMax: Decimal


class RydbergLocal(BaseModel):
    """
    Parameters determining the limitations on the shifting field that shifts the
        Rydberg state energy by a site- and time-dependent amount
    Attributes:
        detuningRange (Tuple[Decimal,Decimal]): Achievable detuning range for
            local detuning patterns (measured in rad/s)
        commonDetuningResolution(Decimal): Resolution with which time-dependent term
            of local detuning can be specified (measured in rad/s)
        localDetuningResolution(Decimal): Resolution with which site-dependent coefficients
            can be specified (unitless)
        detuningSlewRateMax(Decimal): Maximum slew rate for changing the local
            detuning (measured in (rad/s)/s)
        numberLocalDetuningSites (int): Max number of sites available for the local Rydberg
            detuning pattern
        spacingRadialMin (Decimal): Minimum radial spacing between any two sites in the local
            detuning pattern (measured in meters)
        timeResolution(Decimal): Resolution with which times for local Rydberg drive
            parameters can be specified (measured in s)
        timeDeltaMin(Decimal): Minimum time step with which times for local Rydberg drive
            parameters can be specified (measured in s)
    """

    detuningRange: Tuple[Decimal, Decimal]
    commonDetuningResolution: Decimal
    localDetuningResolution: Decimal
    detuningSlewRateMax: Decimal
    numberLocalDetuningSites: int
    spacingRadialMin: Decimal
    timeResolution: Decimal
    timeDeltaMin: Decimal


class Rydberg(BaseModel):
    """
    Parameters determining the limitations of the Rydberg Hamiltonian
    Attributes:
        c6Coefficient (Decimal): Rydberg-Rydberg C6 interaction
            coefficient (measured in (rad/s)*m^6)
        rydbergGlobal: Rydberg Global
        rydbergLocal: Rydberg Local
    """

    c6Coefficient: Decimal
    rydbergGlobal: RydbergGlobal
    rydbergLocal: RydbergLocal


class PerformanceLattice(BaseModel):
    """
    Uncertainties of atomic site arrangements
    Attributes:
        positionErrorAbs (Decimal): Error between target and actual site
            position (measured in meters)
    """

    positionErrorAbs: Decimal


class PerformanceRydbergGlobal(BaseModel):
    """
    Parameters determining the limitations of the global driving field
    Attributes:
        rabiFrequencyErrorRel (Decimal): random error in the Rabi frequency, relative (unitless)
        rabiFrequencyHomogeneityRel (Decimal): fractional RMS Rabi frequency non-uniformity
            across the user area (unitless)
        rabiFrequencyHomogeneityAbs (Decimal): absolute RMS detuning non-uniformity across
            the user area (measured in rad/s)
        detuningErrorAbs (Decimal): random error in the detuning, absolute (measured in rad/s)
        phaseErrorAbs (Decimal): random error in the phase, absolute (measured in rad)
        omegaTau (Decimal): Product of Rabi frequency and Rabi decay time for a single qubit
            under resonan Rydberg drive - average over field of view
            (no local detuning applied) (unitless)
        singleQubitFidelity (Decimal): Single qubit fidelity of a pi(3.14) pulse (unitless)
        twoQubitFidelity (Decimal): Fidelity of two-qubit entangled state (unitless)
    """

    rabiFrequencyErrorRel: Decimal
    rabiFrequencyHomogeneityRel: Decimal
    rabiFrequencyHomogeneityAbs: Decimal
    detuningErrorAbs: Decimal
    phaseErrorAbs: Decimal
    omegaTau: Decimal
    singleQubitFidelity: Decimal
    twoQubitFidelity: Decimal


class PerformanceRydbergLocal(BaseModel):
    """
    Parameters determining the limitations of the shifting field
    Attributes:
        detuningDynamicRange (Decimal): dynamic range over which the specified local
            detuning accuracy is preserved, relative to max detuning used. E.g. if the largest
            local detuning is 2*pi(3.14) *37.0e6 rad/s, detuning accuracy (error) is preserved
            for other sites down to 2*pi(3.14) *3.7e6 (unitless)
        detuningErrorRel (Decimal): random local detuning error, relative to the given local
            detuning (unitless)
        detuningHomogeneity (Decimal): worst-case fractional RMS detuning non-uniformity of the
            detuning pattern, relative to the max detuning used in the detuning pattern;
            applies over the specified dynamic range only (unitless)
        detuningScaleErrorRel (Decimal): error on the global scaling factor for local detuning ,
            relative (unitless)
        darkErrorRete (Decimal): Error rate induced by local detuning pattern under Rydberg
            drive for qubits maximally detuned by the local detuning pattern (scattering)
            (measured in hertz)
        brightErrorRate (Decimal): worst-case error rate induced by local detuning pattern under
            Rydberg drive for qubits minimally detuned by the local detuning pattern
            (scattering from leakage and crosstalk) (measured in hertz)
    """

    detuningDynamicRange: Decimal
    detuningErrorRel: Decimal
    detuningHomogeneity: Decimal
    detuningScaleErrorRel: Decimal
    darkErrorRete: Decimal
    brightErrorRate: Decimal


class PerformanceRydberg(BaseModel):
    """
    Parameters determining the limitations the Rydberg simulator
    Attributes:
        global: Performance of Rydberg Global
        local: Performance of Rydberg Local
    """

    rydbergGlobal: PerformanceRydbergGlobal
    rydbergLocal: PerformanceRydbergLocal


class Detection(BaseModel):
    """
    Parameters determining the accuracy of atom detection
     Attributes:
         atomDetectionFidelity (Decimal): probability of detecting an atom conditioned
             on the atom being there (unitless)
         vacancyDetectionFidelity (Decimal): probability of detecting no atom conditioned
            on the there being no atom (unitless)
         groundStateDetectionFidelity (Decimal): probability of detecting an atom in the
            ground state conditioned on the atom being in the ground state (unitless)
         rydbergStateDetectionFidelity (Decimal): probability of detecting an atom in the
            Rydberg state conditioned on the atom being in the Rydberg state (unitless)
    """

    atomDetectionFidelity: Decimal
    vacancyDetectionFidelity: Decimal
    groundStateDetectionFidelity: Decimal
    rydbergStateDetectionFidelity: Decimal


class Sorting(BaseModel):
    """
    Success probabilities of sorting and arranging
    Attributes:
        moveFidelity (Decimal): Probability for a single sorting move to succeed (unitless)
        patternFidelitySquare (Decimal): Probability of successfully arranging a maximal square
            pattern (256 qubits, filling field of view) (unitless)
    """

    moveFidelity: Decimal
    patternFidelitySquare: Decimal


class Performance(BaseModel):
    """
    Parameters determining the limitations of the QuEra device
    Attributes:
        performanceLattice: Uncertainties of atomic site arrangements
        performanceRydberg : Parameters determining the limitations the Rydberg simulator
        detection : Parameters determining the accuracy of atom detection
        sorting : Success probabilities of sorting and arranging
    """

    lattice: PerformanceLattice
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
        ...             "timeMin": 0,
        ...             "timeMax": 4.0e-6,
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
        ...     "performance": {
        ...         "performanceLattice":{
        ...             "positionErrorAbs": 0.025e-6,
        ...         },
        ...         "performanceRydberg":{
        ...             "performanceRydbergGlobal":{
        ...                 "rabiFrequencyErrorRel:": 0.01,
        ...                 "rabiFrequencyHomogeneityRel": 0.05,
        ...                 "rabiFrequencyHomogeneityAbs": 60e3,
        ...                 "detuningErrorAbs": 60e3,
        ...                 "phaseErrorAbs": 0.005,
        ...                 "omegaTau": 10,
        ...                 "singleQubitFidelity": 0.95,
        ...                 "twoQubitFidelity": 0.95,
        ...             },
        ...             "performanceRydbergLocal":{
        ...                 "detuningDynamicRange:": 10,
        ...                 "detuningErrorRel": 0.01,
        ...                 "detuningHomogeneity": 0.02,
        ...                 "detuningScaleErrorRel": 0.01,
        ...                 "darkErrorRate": 1e3,
        ...                 "brightErrorRate": 3e6,
        ...             }
        ...         },
        ...         "detection":{
        ...                 "atomDetectionFidelity:": 0.99,
        ...                 "vacancyDetectionFidelity": 0.999,
        ...                 "groundStateDetectionFidelity": 0.99,
        ...                 "rydbergStateDetectionFidelity": 0.99,
        ...         },
        ...         "sorting":{
        ...                 "moveFidelity:": 0.98,
        ...                 "patternFidelitySquare": 1e-4,
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
    performance: Performance
