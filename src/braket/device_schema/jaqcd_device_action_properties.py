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

from typing import List, Optional

from braket.device_schema.device_action_properties import DeviceActionProperties


class JaqcdDeviceActionProperties(DeviceActionProperties):

    """
    This defines the schema for properties for the actions that can be supported by the
        jaqcd devices

    Attributes:
        supportedOperations: operations supported by the jaqcd action
        supportedResultTypes: result types that are supported by the jaqcd action.

    Examples:
        >>> import json
        >>> input_json = {
        ...    "actionType": "braket.ir.jaqcd.program",
        ...    "version": ["1.0", "1.1"],
        ...    "supportedOperations": ["x", "y"],
        ...    "supportedResultTypes": ["expectation"],
        ... }
        >>> JaqcdDeviceActionProperties.parse_raw(json.dumps(input_json))

    """

    supportedOperations: List[str]
    supportedResultTypes: Optional[List[str]]
