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

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class PostProcessingType(str, Enum):
    """
    The type of processing for D-Wave.
    """

    RAW = "raw"
    HISTOGRAM = "histogram"


class DwaveProviderLevelParameters(BraketSchemaBase):
    """
    This is the description of the D-Wave parameters

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.dwave.dwave_provider_level_parameters",
        ...        "version": "1",
        ...    },
        ...    "beta": 1
        ... }
        >>> DwaveProviderLevelParameters.parse_raw_schema(json.dumps(input_json))

    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.dwave.dwave_provider_level_parameters", version="1"
    )
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
