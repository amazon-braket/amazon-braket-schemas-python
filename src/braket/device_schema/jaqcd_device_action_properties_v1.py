from typing import Dict, List, Optional, Union

from pydantic import Field

from braket.device_schema.device_action_properties_v1 import DeviceActionProperties
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
from braket.schema_common import BraketSchemaHeader

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

Results = Union[Amplitude, Expectation, Probability, Sample, StateVector, Variance]


class JaqcdDeviceActionProperties(DeviceActionProperties):
    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.jaqcd_device_action_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    supportedOperations: List[GateInstructions]
    supportedResultTypes: Optional[List[Results]]
