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

from pydantic import BaseModel

from braket.device_schema.device_action_properties import DeviceActionProperties, DeviceActionType
from braket.device_schema.device_paradigm_properties_v1 import DeviceParadigmProperties
from braket.device_schema.device_parameters import DeviceParameters
from braket.device_schema.device_service_properties_v1 import DeviceServiceProperties


class DeviceCapabilities(BaseModel):
    """
        DeviceCapabilities are the properties specific to device, this schema defines what is common
        across all the devices

        Attributes:
            service: properties which are common to the braket service
            action: Map of the action to its properties
            paradigm: Provides information on what are the common properties for the device paradigm
            deviceParameters: Device parameters is the schema of input provided to Create quantum task.

        Examples:
            >>> import json
            >>> input_json = {
            ...    "service": {
            ...        "braketSchemaHeader": {
            ...            "name": "braket.device_schema.device_service_properties",
            ...            "version": "1",
            ...        },
            ...        "executionWindows": [
            ...            {
            ...                "executionDay": "Everyday",
            ...                "windowStartHour": "1966280412345.6789",
            ...                "windowEndHour": "1966280414345.6789",
            ...            }
            ...        ],
            ...        "shots": 2,
            ...    },
            ...    "action": {
            ...        "braket.ir.jaqcd.program": {
            ...            "actionType": "braket.ir.jaqcd.program",
            ...            "version": ["1.0", "1.1"],
            ...        }
            ...    },
            ...    "paradigm": {
            ...        "braketSchemaHeader": {
            ...            "name": "braket.device_schema.device_paradigm_properties",
            ...            "version": "1",
            ...        }
            ...    },
            ...    "deviceParameters": {
            ...        "braketSchemaHeader": {
            ...            "name": "braket.device_schema.device_parameters",
            ...            "version": "1",
            ...        },
            ...        "deviceParameters": {
            ...            "braketSchemaHeader": {
            ...                "name": "braket.device_schema.annealing_model_parameters",
            ...                "version": "1",
            ...            },
            ...            "dwaveParameters": {
            ...                "braketSchemaHeader": {
            ...                    "name": "braket.device_schema.dwave_parameters",
            ...                    "version": "1",
            ...                }
            ...            },
            ...        },
            ...    },
            ... }
            >>> DeviceCapabilities.parse_raw(json.dumps(input_json))
    """

    service: DeviceServiceProperties
    action: Dict[DeviceActionType, DeviceActionProperties]
    paradigm: DeviceParadigmProperties
    deviceParameters: DeviceParameters
