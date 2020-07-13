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
# language governing permissions and limitations under the License

from typing import List, Optional

from pydantic import conint, conlist

from braket.ir.annealing import ProblemType
from braket.schema_common.schema_base import BraketSchemaBase
from braket.task_result.additional_metadata import AdditionalMetadata
from braket.task_result.task_metadata import TaskMetadata


class AnnealingTaskResult(BraketSchemaBase):
    """
    The annealing task result schema.

    Attributes:
        solutions (List[int]): solutions of task result
        solutionCounts (List[int]): the number of times the solutions occurred.
            Default is None
        values (List[float]): output or energy of the solutions
        variableCount (int): the number of variables
        taskMetadata (TaskMetadata): the task metadata
        additionalMetadata (AdditionalMetadata): additional metadata of the task

    """

    solutions: List[conlist(conint(ge=-1, le=3), min_items=1)]
    solutionCounts: Optional[List[conint(ge=0)]]
    values: List[float]
    variableCount: conint(ge=0)
    problemType: ProblemType
    taskMetadata: TaskMetadata
    additionalMetadata: AdditionalMetadata
