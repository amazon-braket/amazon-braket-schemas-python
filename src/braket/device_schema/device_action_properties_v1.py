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
from typing import List

from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DeviceActionType(str, Enum):
    """
        These are the actions supported by braket.
    """

    JAQCD = "braket.ir.jaqcd.program"
    ANNEALING = "braket.ir.annealing.problem"


class DeviceActionProperties(BraketSchemaBase):
    """
        This class defines the actions that can be performed by a device

        Attributes:
            version: List of versions for the actions the device supports
            actionType: Enum for the action type. Type of the action to be performed.

        Examples:
            >>> import json
            >>> input_json = {
            ...     "braketSchemaHeader": {
            ...         "name": "braket.device_schema.device_action_properties",
            ...         "version": "1",
            ...     },
            ...     "actionType": "braket.ir.jaqcd.program",
            ...     "version": ["1.0", "1.1"],
            ... }
            >>> DeviceActionProperties.parse_raw_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.device_action_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    version: List[str]
    actionType: DeviceActionType
