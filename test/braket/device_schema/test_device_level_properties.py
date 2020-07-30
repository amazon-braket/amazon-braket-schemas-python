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

from braket.device_schema.device_level_properties import DeviceLevelProperties


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "supportedRegions": ["IAD"],
        "deviceCost": [10, "task"],
        "deviceMetadata": "metadata of the device",
        "deviceLocation": "IAD",
        "summary": "details of the device",
        "externalDocumentation": "details to external doc",
    }
    return input


def test_valid(valid_input):
    result = DeviceLevelProperties.parse_raw(json.dumps(valid_input))
    assert result.supportedRegions == ["IAD"]


@pytest.mark.xfail(raises=ValidationError)
def test__missing_deviceCost(valid_input):
    valid_input.pop("deviceCost")
    assert DeviceLevelProperties.parse_raw(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_deviceMetadata(valid_input):
    valid_input["deviceMetadata"] = 1
    DeviceLevelProperties.parse_raw(json.dumps(valid_input))
