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

from datetime import datetime
from enum import Enum

from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class ExecutionDay(str, Enum):
    """ The type of annealing problem.

    QUBO: Quadratic Unconstrained Binary Optimization, with values 1 and 0
    ISING: Ising model, with values +/-1
    """

    EVERYDAY = "Everyday"
    WEEKDAYS = "Weekdays"
    WEEKENDS = "Weekend"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class DeviceExecutionWindow(BraketSchemaBase):

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.device_execution_window", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    executionDay: ExecutionDay
    windowStartHour: datetime
    windowEndHour: datetime
