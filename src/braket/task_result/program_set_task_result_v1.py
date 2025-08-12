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

from typing import Optional, Union

from pydantic.v1 import Field

from braket.schema_common.schema_base import BraketSchemaBase
from braket.schema_common.schema_header import BraketSchemaHeader
from braket.task_result.program_result_v1 import ProgramResult
from braket.task_result.program_set_task_metadata_v1 import ProgramSetTaskMetadata


class ProgramSetTaskResult(BraketSchemaBase):
    """
    The result of a program set task.

    Attributes:
        programResults (Union[list[str], list[ProgramResult]]): The relative S3 paths
            of the program result files, or a list of the program results themselves.
        s3Location (Optional[tuple[str, str]]): The S3 bucket and prefix where this result
            and all associated files are saved; blank if all data is inlined in the result file.
        taskMetadata (ProgramSetTaskMetadata): The relative S3 paths of the metadata file,
            or the task metadata itself.
    """

    _PROGRAM_SET_TASK_RESULT_HEADER = BraketSchemaHeader(
        name="braket.task_result.program_set_task_result", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(
        default=_PROGRAM_SET_TASK_RESULT_HEADER, const=_PROGRAM_SET_TASK_RESULT_HEADER
    )

    programResults: Union[list[str], list[ProgramResult]]
    taskMetadata: Union[str, ProgramSetTaskMetadata]
    s3Location: Optional[tuple[str, str]]
