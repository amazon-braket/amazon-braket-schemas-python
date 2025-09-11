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

from pydantic.v1 import BaseModel, Field, confloat, conint, conlist, constr

from braket.schema_common.schema_base import BraketSchemaBase
from braket.schema_common.schema_header import BraketSchemaHeader


class ProgramSetExecutableResultMetadata(BaseModel):
    """Metadata for successful program executable."""

    pass


class ProgramSetExecutableResult(BraketSchemaBase):
    """
    The result of a successful program set executable

    Attributes:
        inputsIndex (int): A reference to the inputs the program was run with.
        measurements (List[List[int]]: List of lists, where each list represents a shot
            and each index of the list represents a qubit. Default is `None`.
        measurementProbabilities (dict[str, float]): A dictionary of probabilistic results.
            Key is the measurements in a big endian binary string.
            Value is the probability the measurement occurred.
            Default is `None`.
        measuredQubits (List[int]): The indices of the measured qubits.
            Indicates which qubits are in `measurements`. Default is `None`.
    """

    _PROGRAM_SET_EXECUTABLE_RESULT_HEADER = BraketSchemaHeader(
        name="braket.task_result.program_set_executable_result", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(
        default=_PROGRAM_SET_EXECUTABLE_RESULT_HEADER, const=_PROGRAM_SET_EXECUTABLE_RESULT_HEADER
    )

    inputsIndex: int
    measurements: Optional[Union[conlist(conlist(conint(ge=0, le=1), min_items=1), min_items=1),]]
    measurementProbabilities: Optional[
        dict[constr(regex="^[01]+$", min_length=1), confloat(ge=0, le=1)]
    ]
    measuredQubits: Optional[conlist(conint(ge=0), min_items=1)]
