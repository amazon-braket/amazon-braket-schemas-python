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

import json

import pytest
from pydantic import ValidationError

from braket.device_schema.dwave_device_parameters_v1 import DwaveDeviceParameters


def test_valid():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.dwave_device_parameters",
            "version": "1",
        },
        "deviceLevelParameters": {},
    }
    assert DwaveDeviceParameters.parse_raw_schema(json.dumps(input))


@pytest.mark.xfail(raises=ValidationError)
def test_missing_header():
    input = '{"deviceLevelParameters": {"annealingOffsets": [1]}}'
    DwaveDeviceParameters.parse_raw_schema(input)
