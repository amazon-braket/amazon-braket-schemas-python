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

from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class ProblemType(str, Enum):
    QUBO = "QUBO"
    ISING = "ISING"


class Problem(BraketSchemaBase):
    """Specifies a quantum annealing problem."""

    _PROBLEM_HEADER = BraketSchemaHeader(name="braket.ir.annealing.problem", version="1")
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROBLEM_HEADER)
    type: ProblemType | str
    linear: dict[int, float]
    quadratic: dict[str, float]
