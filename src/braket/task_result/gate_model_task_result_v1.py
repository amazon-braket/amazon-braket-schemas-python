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


from typing import TypeAlias

from pydantic import (
    BaseModel,
    Field,
    StrictBool,
    confloat,
    conint,
    conlist,
    constr,
    field_validator,
)

from braket.ir.jaqcd.program_v1 import Results
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader
from braket.task_result.additional_metadata import AdditionalMetadata
from braket.task_result.task_metadata_v1 import TaskMetadata

StrictInt = conint(strict=True)
StrictFloat = confloat(allow_inf_nan=False, strict=True)

ScalarValue: TypeAlias = StrictBool | StrictInt | StrictFloat
ScalarOrNull: TypeAlias = ScalarValue | None

OutputValue: TypeAlias = (
    ScalarOrNull | list[StrictBool | None] | list[StrictInt | None] | list[StrictFloat | None]
)


class ResultTypeValue(BaseModel):
    """
    Requested result type and value of gate model task result.

    Attributes:
         type (Union[Expectation, Sample, StateVector, Variance, Probability, Amplitude,
            AdjointGradient]): The requested result type
         value (Union[List, float, Dict]): The value of the requested result
    """

    type: Results
    value: list | float | dict


class GateModelTaskResult(BraketSchemaBase):
    """
    The gate model task result schema

    Attributes:
        braketSchemaHeader (BraketSchemaHeader): Schema header. Users do not need
            to set this value. Only default is allowed.
        measurements (list[list[int]]: List of lists, where each list represents a shot
            and each index of the list represents a qubit. Default is `None`.
        measurementProbabilities (dict[str, float]): A dictionary of probabilistic results.
            Key is the measurements in a big endian binary string.
            Value is the probability the measurement occurred.
            Default is `None`.
        measuredQubits (list[int]): The indices of the measured qubits.
            Indicates which qubits are in `measurements`. Default is `None`.
        resultTypes (list[ResultTypeValue]): Requested result types and their values.
            Default is `None`.
        outputs (list[dict[str, OutputValue]]): Per-shot values of OpenQASM 3
            ``output``-declared variables. Each element is one shot, mapping each
            output variable name to its value (a scalar, or a homogeneous list for
            registers). An undefined value is represented by ``None``. Default is
            `None`.
        taskMetadata (TaskMetadata): The task metadata
        additionalMetadata (AdditionalMetadata): Additional metadata of the task
    """

    _GATE_MODEL_TASK_RESULT_HEADER = BraketSchemaHeader(
        name="braket.task_result.gate_model_task_result", version="1"
    )

    braketSchemaHeader: BraketSchemaHeader = Field(default=_GATE_MODEL_TASK_RESULT_HEADER)
    # fmt: off
    measurements: conlist(conlist(conint(ge=0, le=1), min_length=1), min_length=1) | None = None
    # fmt: on
    measurementProbabilities: (
        dict[constr(pattern="^[01]+$", min_length=1), confloat(ge=0, le=1)] | None
    ) = None
    resultTypes: list[ResultTypeValue] | None = None
    measuredQubits: conlist(conint(ge=0), min_length=1) | None = None
    outputs: conlist(dict[constr(min_length=1), OutputValue], min_length=1) | None = None
    taskMetadata: TaskMetadata
    additionalMetadata: AdditionalMetadata

    @field_validator("outputs")
    @classmethod
    def validate_non_empty_shot(cls, outputs):
        """
        Rejects empty per-shot dicts. Every declared output variable appears in
        each shot (its value or None), so an empty shot signals malformed data.

        Args:
            outputs (list[dict] | None): The per-shot outputs list.

        Returns:
            list[dict] | None: The same outputs, with each shot validated to be non-empty.

        Raises:
            ValueError: If any shot dict is empty.
        """
        if outputs is None:
            return outputs
        for shot in outputs:
            if not shot:
                raise ValueError("each output shot must contain at least one variable")
        return outputs
