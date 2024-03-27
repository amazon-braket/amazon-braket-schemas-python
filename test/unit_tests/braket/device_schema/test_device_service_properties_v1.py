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

import pytest
from pydantic.v1 import ValidationError

from braket.device_schema.device_service_properties_v1 import DeviceServiceProperties


@pytest.fixture()
def valid_input():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.device_service_properties",
            "version": "1",
        },
        "executionWindows": [
            {"executionDay": "Everyday", "windowStartHour": "11:00", "windowEndHour": "12:00"}
        ],
        "shotsRange": [1, 10],
        "deviceCost": {"price": 0.25, "unit": "minute"},
        "deviceDocumentation": {
            "imageUrl": "image_url",
            "summary": "Summary on the device",
            "externalDocumentationUrl": "exter doc link",
        },
        "deviceLocation": "us-east-1",
        "updatedAt": "2020-06-16T19:28:02.869136",
    }
    return input


@pytest.fixture()
def valid_input_with_getTaskPollInterval(valid_input):
    valid_input["getTaskPollIntervalMillis"] = 200
    return valid_input


def test_valid(valid_input):
    result = DeviceServiceProperties.parse_raw_schema(json.dumps(valid_input))
    assert result.shotsRange == (1, 10)


@pytest.mark.xfail(raises=ValidationError)
def test__missing_schemaHeader(valid_input):
    valid_input.pop("braketSchemaHeader")
    assert DeviceServiceProperties.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test__missing_executionWindows(valid_input):
    valid_input.pop("executionWindows")
    assert DeviceServiceProperties.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test__missing_shots(valid_input):
    valid_input.pop("shotsRange")
    DeviceServiceProperties.parse_raw_schema(json.dumps(valid_input))


def test_parse_valid_input_without_getTaskPollIntervalMillis(valid_input):
    assert "getTaskPollIntervalMillis" not in valid_input
    service_props = DeviceServiceProperties.parse_raw_schema(json.dumps(valid_input))
    assert not service_props.getTaskPollIntervalMillis


def test_parse_valid_input_with_getTaskPollInterval(valid_input_with_getTaskPollInterval):
    service_props = DeviceServiceProperties.parse_raw_schema(
        json.dumps(valid_input_with_getTaskPollInterval)
    )
    assert service_props.getTaskPollIntervalMillis == 200
