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

from pydantic import BaseModel

from braket.ir.gate_model_shared.shared_models import (
    MultiState,
    Observable,
    OptionalMultiParameter,
    OptionalMultiTarget,
    OptionalNestedMultiTarget,
)


class Expectation(OptionalMultiTarget, Observable):
    class Type(str, Enum):
        expectation = "expectation"

    type: Type = Type.expectation


class AdjointGradient(OptionalNestedMultiTarget, Observable, OptionalMultiParameter):
    class Type(str, Enum):
        adjoint_gradient = "adjoint_gradient"

    type: Type = Type.adjoint_gradient


class Sample(OptionalMultiTarget, Observable):
    class Type(str, Enum):
        sample = "sample"

    type: Type = Type.sample


class Variance(OptionalMultiTarget, Observable):
    class Type(str, Enum):
        variance = "variance"

    type: Type = Type.variance


class StateVector(BaseModel):
    class Type(str, Enum):
        statevector = "statevector"

    type: Type = Type.statevector


class DensityMatrix(OptionalMultiTarget):
    class Type(str, Enum):
        densitymatrix = "densitymatrix"

    type: Type = Type.densitymatrix


class Amplitude(MultiState):
    class Type(str, Enum):
        amplitude = "amplitude"

    type: Type = Type.amplitude


class Probability(OptionalMultiTarget):
    class Type(str, Enum):
        probability = "probability"

    type: Type = Type.probability
