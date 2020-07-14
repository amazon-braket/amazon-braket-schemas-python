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
# language governing permissions and limitations under the License

from typing import Optional

from pydantic import BaseModel, conint, conlist
from braket.schema_common.schema_base import BraketSchemaBase


class DWaveTiming(BaseModel):
    """
    The D-Wave timing metadata result schema.

    The times represented are in milliseconds.

    Examples:
        >>> DWaveTiming(qpuSamplingTime=1575, qpuAnnealTimePerSample=20)
    """

    qpuSamplingTime: Optional[conint(ge=0)]
    qpuAnnealTimePerSample: Optional[conint(ge=0)]
    qpuAccessTime: Optional[conint(ge=0)]
    qpuAccessOverheadTime: Optional[conint(ge=0)]
    qpuReadoutTimePerSample: Optional[conint(ge=0)]
    qpuProgrammingTime: Optional[conint(ge=0)]
    qpuDelayTimePerSample: Optional[conint(ge=0)]
    postProcessingOverheadTime: Optional[conint(ge=0)]
    totalPostProcessingTime: Optional[conint(ge=0)]
    totalRealTime: Optional[conint(ge=0)]
    runTimeChip: Optional[conint(ge=0)]
    annealTimePerRun: Optional[conint(ge=0)]
    readoutTimePerRun: Optional[conint(ge=0)]


class DWaveMetadata(BraketSchemaBase):
    """
    The D-Wave metadata result schema.

    Attributes:
        - activeVariables (List[int]): the active variables of the task on D-Wave
        - timing (DWaveTiming): additional timing metadata of the task on D-Wave

    Examples:
        >>> timing = DWaveTiming(qpuSamplingTime=1575, qpuAnnealTimePerSample=20)
        >>> DWaveMetadata(activeVariables=[0, 3, 4], timing=timing)
    """

    activeVariables: conlist(conint(ge=0))
    timing: DWaveTiming
