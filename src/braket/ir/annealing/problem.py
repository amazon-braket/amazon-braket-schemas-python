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
from typing import Dict, Tuple

from pydantic import BaseModel, conint


class ProblemType(str, Enum):
    """ The type of annealing problem.

    QUBO: Quadratic Unconstrained Binary Optimization, with values 1 and 0
    ISING: Ising model, with values +/-1
    """

    QUBO = "QUBO"
    ISING = "ISING"


class Problem(BaseModel):
    """ Specifies a quantum annealing problem.

    Attributes:
        - type: The type of problem; can be either "QUBO" or "ISING"
        - linear: Linear coefficients of the model, expressed as a map of term
            to coefficient. For example,
                0.3 * x_0 - 0.3 * x_4
            is expressed as
                {0: 0.3, 4: -0.3}
        - quadratic: Quadratic coefficients of the model, expressed as a map of
            the first variable in the term to a map of the second variable to the
            corresponding quadratic term's coefficient. For example,
                0.667 * x_0 * x_5 + 3 * x_0 * x_6 + 0.1 * x_2 * x_4
            is expressed as
                {0: {5: 0.667, 6: 3}, 2: {4: 0.1}}

    Examples:
        >>> Problem(type=ProblemType.QUBO,
        >>>         linear={0: 0.3, 4: -0.3},
        >>>         quadratic={0: {5: 0.667, 6: 3}, 2: {4: 0.1}})
    """

    type: ProblemType
    linear: Dict[conint(ge=0), float]
    quadratic: Dict[Tuple[conint(ge=0), conint(ge=0)], float]
    quadratic: Dict[conint(ge=0), Dict[conint(ge=0), float]]
