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

from typing import Union

from pydantic.v1 import Field

from braket.ir.openqasm import Program
from braket.schema_common.schema_base import BraketSchemaBase
from braket.schema_common.schema_header import BraketSchemaHeader
from braket.task_result.additional_metadata import AdditionalMetadata
from braket.task_result.program_set_executable_failure_v1 import ProgramSetExecutableFailure
from braket.task_result.program_set_executable_result_v1 import ProgramSetExecutableResult


class ProgramResult(BraketSchemaBase):
    """
    The results of single program of a program set.

    Attributes:
        executableResults (Union[list[str], list[ProgramSetExecutableResult | ProgramSetExecutableFailure]]):  # noqa
            The relative S3 paths of the executable result files,
            or a list of the executable results or failures themselves.
        source (Union[str, Program]): The program that was run or the relative S3 path of
            the program file; if the program is parametrized, this includes all input values
            the program was run with.
        additionalMetadata (AdditionalMetadata): Additional metadata of the task.
    """

    _PROGRAM_SET_PROGRAM_RESULT_HEADER = BraketSchemaHeader(
        name="braket.task_result.program_result", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(
        default=_PROGRAM_SET_PROGRAM_RESULT_HEADER, const=_PROGRAM_SET_PROGRAM_RESULT_HEADER
    )

    executableResults: Union[
        list[str], list[Union[ProgramSetExecutableResult, ProgramSetExecutableFailure]]
    ]
    source: Union[str, Program]
    additionalMetadata: AdditionalMetadata
