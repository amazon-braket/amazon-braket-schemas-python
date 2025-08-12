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

from enum import Enum

from pydantic.v1 import BaseModel, Field

from braket.schema_common.schema_base import BraketSchemaBase
from braket.schema_common.schema_header import BraketSchemaHeader


class FailureCategory(str, Enum):
    COMPILATION = "COMPILATION"
    DEVICE = "DEVICE"
    SERVICE = "SERVICE"


class ProgramSetExecutableFailureMetadata(BaseModel):
    """
    Attributes:
        failureReason (str): The reason stating why the executable failed.
        retryable (bool): Indicates whether the executable can be retried.
        category (FailureCategory): The enum representing where the executable failed.
    """

    failureReason: str
    retryable: bool
    category: FailureCategory


class ProgramSetExecutableFailure(BraketSchemaBase):
    """
    Represents a failed program set executable.

    Attributes:
        inputsIndex (int): A reference to the inputs the program was run with.
        failureMetadata (ProgramSetExecutableFailureMetadata): Metadata about the failure
            of the executable
    """

    _EXECUTABLE_FAILURE_HEADER = BraketSchemaHeader(
        name="braket.task_result.program_set_executable_failure", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(
        default=_EXECUTABLE_FAILURE_HEADER, const=_EXECUTABLE_FAILURE_HEADER
    )

    inputsIndex: int
    failureMetadata: ProgramSetExecutableFailureMetadata
