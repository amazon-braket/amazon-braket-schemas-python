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

from typing import Dict

from pydantic import Field

from braket.device_schema.device_action_properties_v1 import (
    DeviceActionProperties,
    DeviceActionType,
)
from braket.device_schema.device_paradigm_properties_v1 import DeviceParadigmProperties
from braket.device_schema.device_parameters_v1 import DeviceParameters
from braket.device_schema.device_service_properties_v1 import DeviceServiceProperties
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DeviceCapabilities(BraketSchemaBase):

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.device_capabilities", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    service: DeviceServiceProperties
    action: Dict[DeviceActionType, DeviceActionProperties]
    paradigm: DeviceParadigmProperties
    deviceParameters: DeviceParameters
