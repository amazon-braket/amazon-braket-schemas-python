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
# language governing permissions and limitations under the License.

from enum import Enum
from typing import Literal

from pydantic import BaseModel


class Control(BaseModel):
    name: Literal["ctrl"]
    max_qubits: int | None = None


class NegControl(BaseModel):
    name: Literal["negctrl"]
    max_qubits: int | None = None


class ExponentType(str, Enum):
    INT = "int"
    FLOAT = "float"


class Power(BaseModel):
    name: Literal["pow"]
    exponent_types: list[ExponentType]


class Inverse(BaseModel):
    name: Literal["inv"]


Modifier = Control | NegControl | Power | Inverse
