from typing import List

from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DwaveDeviceProperties(BraketSchemaBase):

    """

    This defines the properties specific to dwave device

    Attributes:
        qubits: the list of the qubits available in dwave
        qubitCount: number of qubits available in dwave
        topology: the connections between each qubits

    Examples:
    {
        "braketSchemaHeader": {
            "name": "braket.device_schema.dwave_device_properties",
            "version": "1",
        },
        "annealingOffsetStep": 1.45,
        "annealingOffsetStepPhi0": 1.45,
        "annealingOffsetRanges": [[1.45, 1.45], [1.45, 1.45]],
        "annealingDurationRange": [1, 2, 3],
        "couplers": [[1, 2, 3], [1, 2, 3]],
        "defaultAnnealingDuration": 1,
        "defaultProgrammingThermalizationDuration": 1,
        "defaultReadoutThermalizationDuration": 1,
        "extendedJRange": [1, 2, 3],
        "hGainScheduleRange": [1, 2, 3],
        "hRange": [1, 2, 3],
        "jRange": [1, 2, 3],
        "maximumAnnealingSchedulePoints": 1,
        "maximumHGainSchedulePoints": 1,
        "perQubitCouplingRange": [1, 2, 3],
        "programmingThermalizationDurationRange": [1, 2, 3],
        "qubits": [1, 2, 3],
        "qubitCount": 1,
        "quotaConversionRate": 1,
        "readoutThermalizationDurationRange": [1, 2, 3],
        "taskRunDurationRange": [1, 2, 3],
        "topology": {},
    }
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.dwave_device_properties", version="1"
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
