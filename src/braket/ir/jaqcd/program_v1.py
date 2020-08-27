# Copyright 2019-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

from typing import List, Optional, Union

from pydantic import Field

from braket.ir.jaqcd.instructions import (
    CY,
    CZ,
    XX,
    XY,
    YY,
    ZZ,
    AmplitudeDamping,
    BitFlip,
    CCNot,
    CNot,
    CPhaseShift,
    CPhaseShift00,
    CPhaseShift01,
    CPhaseShift10,
    CSwap,
    Depolarizing,
    H,
    I,
    ISwap,
    Kraus,
    PhaseDamping,
    PhaseFlip,
    PhaseShift,
    PSwap,
    Rx,
    Ry,
    Rz,
    S,
    Si,
    Swap,
    T,
    Ti,
    Unitary,
    V,
    Vi,
    X,
    Y,
    Z,
)
from braket.ir.jaqcd.results import (
    Amplitude,
    DensityMatrix,
    Expectation,
    Probability,
    Sample,
    StateVector,
    Variance,
)
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader

GateInstructions = Union[
    CCNot,
    CNot,
    CPhaseShift,
    CPhaseShift00,
    CPhaseShift01,
    CPhaseShift10,
    CSwap,
    CY,
    CZ,
    H,
    I,
    ISwap,
    PhaseShift,
    PSwap,
    Rx,
    Ry,
    Rz,
    S,
    Swap,
    Si,
    T,
    Ti,
    Unitary,
    V,
    Vi,
    X,
    XX,
    XY,
    Y,
    YY,
    Z,
    ZZ,
]

NoiseInstructions = Union[
    BitFlip,
    PhaseFlip,
    Depolarizing,
    AmplitudeDamping,
    PhaseDamping,
    Kraus,
]

Results = Union[Amplitude, Expectation, Probability, Sample, StateVector, DensityMatrix, Variance]


class Program(BraketSchemaBase):
    """
    Root object of the JsonAwsQuantumCircuitDescription IR.



    Attributes:
        braketSchemaHeader (BraketSchemaHeader): Schema header. Users do not need
            to set this value. Only default is allowed.
        instructions (List[Union[GateInstructions, NoiseInstructions]]): List of instructions.
        basis_rotation_instructions (List[GateInstructions]): List of
            instructions for rotation to desired measurement bases. Default is None.
        results (List[Union[Amplitude, Expectation, Probability, Sample, StateVector, Variance]]):
            List of requested results. Default is None.

    Examples:
        >>> Program(instructions=[H(target=0), Rz(angle=0.15, target=1)])
        >>> Program(instructions=[H(target=0), CNot(control=0, target=1)],
        ...     results=[Expectation(targets=[0], observable=['x'])],
        ...     basis_rotation_instructions=[H(target=0)])


    Note:
        The type `GateInstructions` includes the following instructions:
        CCNot,
        CNot,
        CPhaseShift,
        CPhaseShift00,
        CPhaseShift01,
        CPhaseShift10,
        CSwap,
        CY,
        CZ,
        H,
        I,
        ISwap,
        PhaseShift,
        PSwap,
        Rx,
        Ry,
        Rz,
        S,
        Swap,
        Si,
        T,
        Ti,
        Unitary,
        V,
        Vi,
        X,
        XX,
        XY,
        Y,
        YY,
        Z,
        ZZ

        The type `NoiseInstructions` includes the following instructions:
        BitFlip,
        PhaseDamping
        PhaseFlip,
        Depolarizing,
        AmplitudeDamping,
        Kraus,
    """

    _PROGRAM_HEADER = BraketSchemaHeader(name="braket.ir.jaqcd.program", version="1")
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    instructions: List[Union[GateInstructions, NoiseInstructions]]
    results: Optional[List[Results]]
    basis_rotation_instructions: Optional[List[GateInstructions]]
