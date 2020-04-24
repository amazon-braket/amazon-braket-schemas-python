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

from braket.ir.jaqcd.instructions import (
    CY,
    CZ,
    XX,
    XY,
    YY,
    ZZ,
    CCNot,
    CNot,
    CPhaseShift,
    CPhaseShift00,
    CPhaseShift01,
    CPhaseShift10,
    CSwap,
    H,
    I,
    ISwap,
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
    Expectation,
    Probability,
    Sample,
    StateVector,
    Variance,
)
from pydantic import BaseModel

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


class Program(BaseModel):
    """
    Root object of the JsonAwsQuantumCircuitDescription IR.

    Attributes:
        - instructions: List of instructions.
        - basis_rotation_instructions: List of instructions for rotation to desired measurement
            bases
        - results: List of requested results

    Examples:
        >>> Program(instructions=[H(target=0), Rz(angle=0.15, target=1)])
        >>> Program(instructions=[H(target=0), CNot(control=0, target=1)],
        ...     results=[Expectation(targets=[0], observable=['x'])],
        ...     basis_rotation_instructions=[H(target=0)])
    """

    instructions: List[GateInstructions]
    results: Optional[
        List[Union[Amplitude, Expectation, Probability, Sample, StateVector, Variance]]
    ]
    basis_rotation_instructions: Optional[List[GateInstructions]]
