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

from pydantic import BaseModel


class DeviceLevelProperties(BaseModel):
    """
        DeviceCapabilities are the properties specific to device, this schema defines what is common
        across all the devices

        Attributes:
            supportedRegions: List of the regions a device can support
            deviceCost: cost of the device in USA $ . showed as [cost, factor] eg: [10, "min"]
            deviceMetadata: device metadata
            deviceLocation: Location of the device.
            summary: Description of the device.
            externalDocumentation: Documentation provided by the device provider.

        Examples:
            >>> import json
            >>> input_json = {
            ...     "supportedRegions": ["IAD"],
            ...     "deviceCost": [10, "task"],
            ...     "deviceMetadata": "metadata of the device",
            ...     "deviceLocation": "IAD",
            ...     "summary": "details of the device",
            ...     "externalDocumentation": "details to external doc",
            ... }
            >>> DeviceLevelProperties.parse_raw(json.dumps(input_json))
    """

    supportedRegions: List[str]
    deviceCost: Tuple[int, str]
    deviceMetadata: str
    deviceLocation: str
    summary: str
    externalDocumentation: str
