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

from typing import Annotated

from pydantic import BaseModel, Field, model_validator


class SingleTarget(BaseModel):
    target: Annotated[int, Field(ge=0)]


class DoubleTarget(BaseModel):
    targets: Annotated[list[Annotated[int, Field(ge=0)]], Field(min_length=2, max_length=2)]


class MultiTarget(BaseModel):
    targets: Annotated[list[Annotated[int, Field(ge=0)]], Field(min_length=1)]


class OptionalMultiTarget(BaseModel):
    targets: Annotated[list[Annotated[int, Field(ge=0)]], Field(min_length=1)] | None = None


class OptionalNestedMultiTarget(BaseModel):
    targets: (
        Annotated[
            list[Annotated[list[Annotated[int, Field(ge=0)]], Field(min_length=1)]],
            Field(min_length=1),
        ]
        | None
    ) = None


class OptionalMultiParameter(BaseModel):
    parameters: list[Annotated[str, Field(min_length=1)]] | None = None


class MultiControl(BaseModel):
    controls: Annotated[list[Annotated[int, Field(ge=0)]], Field(min_length=1)]


class DoubleControl(BaseModel):
    controls: Annotated[list[Annotated[int, Field(ge=0)]], Field(min_length=2, max_length=2)]


class SingleControl(BaseModel):
    control: Annotated[int, Field(ge=0)]


class Angle(BaseModel):
    angle: float


class SingleProbability(BaseModel):
    probability: Annotated[float, Field(ge=0.0, le=0.5)]


class SingleProbability_34(BaseModel):
    probability: Annotated[float, Field(ge=0.0, le=0.75)]


class SingleProbability_1516(BaseModel):
    probability: Annotated[float, Field(ge=0.0, le=0.9375)]


class DampingProbability(BaseModel):
    gamma: Annotated[float, Field(ge=0.0, le=1.0)]


class DampingSingleProbability(BaseModel):
    probability: Annotated[float, Field(ge=0.0, le=1.0)]


class TripleProbability(BaseModel):
    probX: Annotated[float, Field(ge=0.0, le=1.0)]
    probY: Annotated[float, Field(ge=0.0, le=1.0)]
    probZ: Annotated[float, Field(ge=0.0, le=1.0)]

    @model_validator(mode="after")
    def validate_probabilities(self):
        if self.probX + self.probY + self.probZ > 1:
            raise ValueError("Sum of probabilities cannot exceed 1.")
        return self


class MultiProbability(BaseModel):
    probabilities: dict[
        Annotated[str, Field(pattern=r"^[IXYZ]+$", min_length=1)],
        Annotated[float, Field(ge=0.0, le=1.0)],
    ]

    @model_validator(mode="after")
    def validate_probabilities(self):
        probabilities = self.probabilities
        if not probabilities:
            raise ValueError("Pauli dictionary must not be empty.")

        qubit_count = len(next(iter(probabilities)))

        if qubit_count * "I" in probabilities:
            i = qubit_count * "I"
            raise ValueError(
                f"{i} is not allowed as a key. Please enter only non-identity Pauli strings."
            )

        for pauli_string in probabilities:
            if len(pauli_string) != qubit_count:
                raise ValueError("Length of each Pauli string must be equal to number of qubits.")

        total_prob = sum(probabilities.values())
        if total_prob > 1.0 or total_prob < 0.0:
            raise ValueError(
                f"Total probability must be a real number in the interval [0, 1]. Total probability was {total_prob}."
            )

        return self


class TwoDimensionalMatrix(BaseModel):
    matrix: Annotated[
        list[
            Annotated[
                list[Annotated[list[float], Field(min_length=2, max_length=2)]], Field(min_length=1)
            ]
        ],
        Field(min_length=1),
    ]


class TwoDimensionalMatrixList(BaseModel):
    matrices: Annotated[
        list[
            Annotated[
                list[
                    Annotated[
                        list[Annotated[list[float], Field(min_length=2, max_length=2)]],
                        Field(min_length=1, max_length=4),
                    ]
                ],
                Field(min_length=1, max_length=4),
            ]
        ],
        Field(min_length=1, max_length=16),
    ]


class Observable(BaseModel):
    observable: (
        Annotated[
            list[
                Annotated[str, Field(pattern=r"^(x|y|z|h|i)$")]
                | Annotated[
                    list[
                        Annotated[
                            list[Annotated[list[float], Field(min_length=2, max_length=2)]],
                            Field(min_length=2),
                        ]
                    ],
                    Field(min_length=2),
                ]
            ],
            Field(min_length=1),
        ]
        | Annotated[str, Field(min_length=1)]
    )


class MultiState(BaseModel):
    states: Annotated[
        list[Annotated[str, Field(pattern=r"^[01]+$", min_length=1)]], Field(min_length=1)
    ]


class CompilerDirective(BaseModel):
    directive: Annotated[str, Field(pattern=r"^(Start|End)VerbatimBlock$")]
