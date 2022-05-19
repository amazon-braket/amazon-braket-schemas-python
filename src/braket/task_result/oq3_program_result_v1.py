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

from typing import Dict, List, Optional

from pydantic import Field, conint, conlist, constr

from braket.ir.openqasm.program_v1 import io_type
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader
from braket.task_result import ResultTypeValue
from braket.task_result.additional_metadata import AdditionalMetadata
from braket.task_result.task_metadata_v1 import TaskMetadata


class OQ3ProgramResult(BraketSchemaBase):
    _OQ3_PROGRAM_RESULT_HEADER = BraketSchemaHeader(
        name="braket.task_result.oq3_program_result", version="1"
    )

    braketSchemaHeader: BraketSchemaHeader = Field(
        default=_OQ3_PROGRAM_RESULT_HEADER, const=_OQ3_PROGRAM_RESULT_HEADER
    )
    outputVariables: Optional[Dict[constr(min_length=1), List[io_type]]]
    resultTypes: Optional[List[ResultTypeValue]]
    taskMetadata: TaskMetadata
    additionalMetadata: AdditionalMetadata
    measurements: Optional[conlist(conlist(conint(ge=0, le=1), min_items=1), min_items=1)]
    measuredQubits: Optional[conlist(conint(ge=0), min_items=1)]
