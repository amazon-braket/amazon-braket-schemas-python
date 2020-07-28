from enum import Enum
from typing import List, Optional

from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class PostProcessingType(str, Enum):
    """
    The type of processing for d wave.
    """

    RAW = "raw"
    HISTOGRAM = "histogram"


class DwaveParameters(BraketSchemaBase):
    """
    This is the description of the d-wave parameters

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.dwave_parameters",
        ...        "version": "1"
        ...    },
        ...    "annealingOffsets": 1
        ... }
        >>> DwaveParameters.parse_raw_schema(json.dumps(input_json))

    """

    _PROGRAM_HEADER = BraketSchemaHeader(name="braket.device_schema.dwave_parameters", version="1")
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    annealingOffsets: Optional[List[int]]
    annealingSchedule: Optional[List[List[int]]]
    annealingDuration: Optional[int] = Field(gt=1)
    autoScale: Optional[bool]
    beta: Optional[int]
    chains: Optional[List[List[int]]]
    compensateFluxDrift: Optional[bool]
    fluxBiases: Optional[List[int]]
    initialState: Optional[List[int]]
    maxResults: Optional[int] = Field(gt=1)
    postprocessingType: Optional[PostProcessingType]
    programmingThermalizationDuration: Optional[int]
    readoutThermalizationDuration: Optional[int]
    reduceIntersampleCorrelation: Optional[bool]
    reinitializeState: Optional[bool]
    resultFormat: Optional[str]
    spinReversalTransformCount: Optional[int] = Field(gt=0)
