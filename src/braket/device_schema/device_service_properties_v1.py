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

from typing import List, Tuple

from pydantic import Field

from braket.device_schema.device_execution_window import DeviceExecutionWindow
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DeviceServiceProperties(BraketSchemaBase):
    """
    This class defines the common service properties for each device.

    Attributes:
        executionWindows: List of the executionWindows, it tells us which days the device can
            execute a task.
        shotsRange: range of the shots for a given device.

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.device_service_properties",
        ...        "version": "1",
        ...    },
        ...    "executionWindows": [
        ...        {
        ...            "executionDay": "Everyday",
        ...            "windowStartHour": "1966280412345.6789",
        ...            "windowEndHour": "1966280414345.6789",
        ...        }
        ...    ],
        ...    "shotsRange": [1,10],
        ... }
        >>> DeviceServiceProperties.parse_raw_schema(json.dumps(input_json))

    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.device_service_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    executionWindows: List[DeviceExecutionWindow]
    shotsRange: Tuple[int, int]
