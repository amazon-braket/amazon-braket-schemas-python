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

from typing import Union

from pydantic.v1 import Field

from braket.device_schema.aqt.aqt_provider_properties_v1 import AqtProviderProperties
from braket.device_schema.device_action_properties import DeviceActionType
from braket.device_schema.device_capabilities import DeviceCapabilities
from braket.device_schema.gate_model_qpu_paradigm_properties_v1 import (
    GateModelQpuParadigmProperties,
)
from braket.device_schema.openqasm_device_action_properties import OpenQASMDeviceActionProperties
from braket.device_schema.openqasm_program_set_device_action_properties import (
    OpenQASMProgramSetDeviceActionProperties,
)
from braket.device_schema.standardized_gate_model_qpu_device_properties_v3 import (
    StandardizedGateModelQpuDeviceProperties,
)
from braket.schema_common.schema_base import BraketSchemaBase
from braket.schema_common.schema_header import BraketSchemaHeader


class AqtDeviceCapabilities(BraketSchemaBase, DeviceCapabilities):
    """
    This defines the capabilities of an AQT device.

    Attributes:
        action(Dict[Union[DeviceActionType, str],
            Union[OpenQASMDeviceActionProperties]]): Actions that an AQT device can support
        paradigm(GateModelQpuParadigmProperties): gate model properties
        provider(Optional[AQTProviderProperties]): AQT provider specific properties
        standardized
            (StandardizedGateModelQpuDeviceProperties): Braket standardized properties for gate model devices
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.aqt.aqt_device_capabilities", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    action: dict[
        Union[DeviceActionType, str],
        Union[OpenQASMDeviceActionProperties, OpenQASMProgramSetDeviceActionProperties],
    ]
    paradigm: GateModelQpuParadigmProperties
    provider: AqtProviderProperties
    standardized: StandardizedGateModelQpuDeviceProperties
