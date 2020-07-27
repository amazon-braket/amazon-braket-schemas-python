from typing import List

from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DWaveDeviceProperties(BraketSchemaBase):
    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.d_wave_device_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    annealingOffsetStep: float
    annealingOffsetStepPhi0: float
    annealingOffsetRanges: List[List[float]]
    annealingDurationRange: List[int]
    couplers: List[List[int]]
    defaultAnnealingDuration: int
    defaultProgrammingThermalizationDuration: int
    defaultReadoutThermalizationDuration: int
    extendedJRange: List[int]
    hGainScheduleRange: List[int]
    hRange: List[int]
    jRange: List[int]
    maximumAnnealingSchedulePoints: int
    maximumHGainSchedulePoints: int
    perQubitCouplingRange: List[int]
    programmingThermalizationDurationRange: List[int]
    qubits: List[int]
    qubitCount: int
    quotaConversionRate: int
    readoutThermalizationDurationRange: List[int]
    taskRunDurationRange: List[int]
    topology: dict
