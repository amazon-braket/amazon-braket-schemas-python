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

from braket.device_schema.device_paradigm_properties_v1 import DeviceParadigmProperties


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.device_paradigm_properties",
            "version": "1",
        }
    }
    return input


def test_valid(valid_input):
    result = DeviceParadigmProperties.parse_raw_schema(json.dumps(valid_input))
    assert result.braketSchemaHeader.name == "braket.device_schema.device_paradigm_properties"


@pytest.mark.xfail(raises=ValidationError)
def test_missing_schema_header(valid_input):
    valid_input.pop("braketSchemaHeader")
    DeviceParadigmProperties.parse_raw_schema(json.dumps(valid_input))
