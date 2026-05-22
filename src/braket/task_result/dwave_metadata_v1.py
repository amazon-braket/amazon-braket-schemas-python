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
# language governing permissions and limitations under the License


from typing import Annotated

from pydantic import BaseModel, Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DwaveTiming(BaseModel):
    """
    The D-Wave timing metadata result schema.

    The times represented are in microseconds.

    Examples:
        >>> DwaveTiming(qpuSamplingTime=1575, qpuAnnealTimePerSample=20)
    """

    qpuSamplingTime: Annotated[int, Field(ge=0)] | None = None
    qpuAnnealTimePerSample: Annotated[int, Field(ge=0)] | None = None
    qpuAccessTime: Annotated[int, Field(ge=0)] | None = None
    qpuAccessOverheadTime: Annotated[int, Field(ge=0)] | None = None
    qpuReadoutTimePerSample: Annotated[int, Field(ge=0)] | None = None
    qpuProgrammingTime: Annotated[int, Field(ge=0)] | None = None
    qpuDelayTimePerSample: Annotated[int, Field(ge=0)] | None = None
    postProcessingOverheadTime: Annotated[int, Field(ge=0)] | None = None
    totalPostProcessingTime: Annotated[int, Field(ge=0)] | None = None
    totalRealTime: Annotated[int, Field(ge=0)] | None = None
    runTimeChip: Annotated[int, Field(ge=0)] | None = None
    annealTimePerRun: Annotated[int, Field(ge=0)] | None = None
    readoutTimePerRun: Annotated[int, Field(ge=0)] | None = None


class DwaveMetadata(BraketSchemaBase):
    """
    The D-Wave metadata result schema.

    Attributes:
        braketSchemaHeader (BraketSchemaHeader): Schema header. Users do not need
            to set this value. Only default is allowed.
        activeVariables (List[int]): The active variables of the task on D-Wave
        timing (DwaveTiming): Additional timing metadata of the task on D-Wave

    Examples:
        >>> timing = DwaveTiming(qpuSamplingTime=1575, qpuAnnealTimePerSample=20)
        >>> DwaveMetadata(activeVariables=[0, 3, 4], timing=timing)
    """

    _DWAVE_METADATA_HEADER = BraketSchemaHeader(
        name="braket.task_result.dwave_metadata", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_DWAVE_METADATA_HEADER)
    activeVariables: list[Annotated[int, Field(ge=0)]]
    timing: DwaveTiming
