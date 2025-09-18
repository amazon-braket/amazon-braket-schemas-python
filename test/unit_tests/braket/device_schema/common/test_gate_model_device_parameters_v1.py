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
# language governing permissions and limitations under the License.

import json

from braket.device_schema.common.gate_model_device_parameters_v1 import GateModelDeviceParameters


def test_common_gate_model_device_parameters():
    input_json = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.common.gate_model_device_parameters",
            "version": "1",
        },
        "paradigmParameters": {
            "braketSchemaHeader": {
                "name": "braket.device_schema.gate_model_parameters",
                "version": "1"
            },
            "qubitCount": 10},
        }
    GateModelDeviceParameters.parse_raw_schema(json.dumps(input_json))