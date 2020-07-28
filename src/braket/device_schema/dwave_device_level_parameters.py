from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class PostProcessingType(str, Enum):
    """
    The type of processing for d wave.
    """

    RAW = "raw"
    HISTOGRAM = "histogram"


class DwaveDeviceLevelParameters(BaseModel):
    """
    This is the description of the d-wave parameters

    Examples:
        >>> import json
        >>> input_json = {
        ...    "beta": 1
        ... }
        >>> DwaveDeviceLevelParameters.parse_raw(json.dumps(input_json))

    """

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
