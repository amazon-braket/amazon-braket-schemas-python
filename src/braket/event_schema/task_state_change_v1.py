# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

from typing import Optional

from pydantic import Field, conint, constr
from typing_extensions import Literal

from braket.event_schema.event_base_v1 import BraketBaseEvent
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class BraketTaskStateChangeDetail(BraketSchemaBase):
    """
    The schema for a task state change event

    Attributes:
        braketSchemaHeader (BraketSchemaHeader): Schema header. Users do not need
            to set this value. Only default is allowed
        quantumTaskArn (str): The task for which this event was generated
        status (Optional[str]): The status that the task transitioned to
        deviceArn (str): The device for which this task was created. Specified by the user
        shots (str): The number of shots requested by the user
        outputS3Bucket (str): The output bucket specified by the user
        outputS3KeyPrefix (str): The output key prefix specified by the user
        createdAt (str): Task creation time as an ISO-8601 string
        endedAt (Optional[str]): The time at which the task reached a terminal state.
            This field is present only when the task has transitioned to a terminal state
    """

    _TASK_STATE_CHANGE_HEADER = BraketSchemaHeader(
        name="braket.event.task.state_change", version="1.0"
    )

    braketSchemaHeader: BraketSchemaHeader = Field(
        default=_TASK_STATE_CHANGE_HEADER, const=_TASK_STATE_CHANGE_HEADER
    )
    quantumTaskArn: constr(min_length=1)
    status: constr(min_length=1, max_length=20)
    deviceArn: constr(min_length=1)
    shots: conint(ge=0)
    outputS3Bucket: constr(min_length=1)
    outputS3KeyPrefix: constr(min_length=1)
    createdAt: constr(regex=r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z")
    endedAt: Optional[constr(regex=r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z")]


TASK_STATE_CHANGE_DETAIL_TYPE = "Braket Task State Change"


class BraketTaskStateChangeEvent(BraketBaseEvent):
    detailType: Literal[TASK_STATE_CHANGE_DETAIL_TYPE] = TASK_STATE_CHANGE_DETAIL_TYPE
    detail: BraketTaskStateChangeDetail
