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

from typing import Any, Union

from pydantic import BaseModel, Field, field_validator

from braket.ir.jaqcd.instructions import (
    CV,
    CY,
    CZ,
    ECR,
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
    EndVerbatimBox,
    GeneralizedAmplitudeDamping,
    H,
    I,
    ISwap,
    Kraus,
    PauliChannel,
    PhaseDamping,
    PhaseFlip,
    PhaseShift,
    PSwap,
    Rx,
    Ry,
    Rz,
    S,
    Si,
    StartVerbatimBox,
    Swap,
    T,
    Ti,
    TwoQubitDephasing,
    TwoQubitDepolarizing,
    Unitary,
    V,
    Vi,
    X,
    Y,
    Z,
)
from braket.ir.jaqcd.results import (
    AdjointGradient,
    Amplitude,
    DensityMatrix,
    Expectation,
    Probability,
    Sample,
    StateVector,
    Variance,
)
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader

_valid_gates = {
    CCNot.Type.ccnot: CCNot,
    CNot.Type.cnot: CNot,
    CPhaseShift.Type.cphaseshift: CPhaseShift,
    CPhaseShift00.Type.cphaseshift00: CPhaseShift00,
    CPhaseShift01.Type.cphaseshift01: CPhaseShift01,
    CPhaseShift10.Type.cphaseshift10: CPhaseShift10,
    CSwap.Type.cswap: CSwap,
    CV.Type.cv: CV,
    CY.Type.cy: CY,
    CZ.Type.cz: CZ,
    ECR.Type.ecr: ECR,
    H.Type.h: H,
    I.Type.i: I,
    ISwap.Type.iswap: ISwap,
    PhaseShift.Type.phaseshift: PhaseShift,
    PSwap.Type.pswap: PSwap,
    Rx.Type.rx: Rx,
    Ry.Type.ry: Ry,
    Rz.Type.rz: Rz,
    S.Type.s: S,
    Swap.Type.swap: Swap,
    Si.Type.si: Si,
    T.Type.t: T,
    Ti.Type.ti: Ti,
    Unitary.Type.unitary: Unitary,
    V.Type.v: V,
    Vi.Type.vi: Vi,
    X.Type.x: X,
    XX.Type.xx: XX,
    XY.Type.xy: XY,
    Y.Type.y: Y,
    YY.Type.yy: YY,
    Z.Type.z: Z,
    ZZ.Type.zz: ZZ,
}

_valid_noise_channels = {
    BitFlip.Type.bit_flip: BitFlip,
    PhaseFlip.Type.phase_flip: PhaseFlip,
    Depolarizing.Type.depolarizing: Depolarizing,
    AmplitudeDamping.Type.amplitude_damping: AmplitudeDamping,
    GeneralizedAmplitudeDamping.Type.generalized_amplitude_damping: GeneralizedAmplitudeDamping,
    PauliChannel.Type.pauli_channel: PauliChannel,
    PhaseDamping.Type.phase_damping: PhaseDamping,
    TwoQubitDephasing.Type.two_qubit_dephasing: TwoQubitDephasing,
    TwoQubitDepolarizing.Type.two_qubit_depolarizing: TwoQubitDepolarizing,
    Kraus.Type.kraus: Kraus,
}

_valid_compiler_directives = {
    StartVerbatimBox.Type.start_verbatim_box: StartVerbatimBox,
    EndVerbatimBox.Type.end_verbatim_box: EndVerbatimBox,
}

Results = Union[
    Amplitude,
    Expectation,
    Probability,
    Sample,
    StateVector,
    DensityMatrix,
    Variance,
    AdjointGradient,
]


class Program(BraketSchemaBase):
    """
    Root object of the JsonAwsQuantumCircuitDescription IR.

    Attributes:
        braketSchemaHeader (BraketSchemaHeader): Schema header. Users do not need
            to set this value. Only default is allowed.
        instructions (List[Any]): List of instructions.
        basis_rotation_instructions (List[Any]): List of instructions for
            rotation to desired measurement bases. Default is None.
        results (List[Results]): List of requested results. Default is None.
    """

    _PROGRAM_HEADER = BraketSchemaHeader(name="braket.ir.jaqcd.program", version="1")
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER)
    instructions: list[Any]
    results: list[Results] | None = None
    basis_rotation_instructions: list[Any] | None = None

    @field_validator("instructions", "basis_rotation_instructions", mode="before")
    @classmethod
    def validate_instructions(cls, value):
        """O(1) deserialization via type-based dispatch."""
        if value is None:
            return value
        return [cls._validate_single_instruction(item) for item in value]

    @classmethod
    def _validate_single_instruction(cls, value):
        if isinstance(value, BaseModel):
            return value
        if isinstance(value, dict) and "type" in value:
            type_val = value["type"]
            if type_val in _valid_gates:
                return _valid_gates[type_val].model_validate(value)
            if type_val in _valid_noise_channels:
                return _valid_noise_channels[type_val].model_validate(value)
            if type_val in _valid_compiler_directives:
                return _valid_compiler_directives[type_val].model_validate(value)
            raise ValueError(f"Invalid instruction type: {type_val}")
        raise ValueError(f"Invalid instruction: {value}")
