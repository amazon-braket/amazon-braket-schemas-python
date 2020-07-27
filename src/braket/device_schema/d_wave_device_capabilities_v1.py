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

from pydantic import Field

from braket.device_schema.annealing_model_parameters_v1 import AnnealingModelParameters
from braket.device_schema.d_wave_device_properties_v1 import DWaveDeviceProperties
from braket.device_schema.device_capabilities_v1 import DeviceCapabilities
from braket.schema_common import BraketSchemaHeader


class DWaveDeviceCapabilities(DeviceCapabilities):

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.d_wave_device_capabilities", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    device: DWaveDeviceProperties
    deviceParameters: AnnealingModelParameters
