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

from braket.device_schema.rigetti.rigetti_provider_properties_v2 import RigettiProviderProperties


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.rigetti.rigetti_provider_properties",
            "version": "2",
        },
        "specs": {
            "name": "Ankaa-9Q-3",
            "architecture": {
                "family": "Ankaa",
                "nodes": [{"node_id": 0}, {"node_id": 1}],
                "edges": [{"node_ids": [0, 1]}],
            },
            "instructions": [
                {
                    "name": "I",
                    "node_count": 1,
                    "parameters": [],
                    "sites": [{"node_ids": [0], "characteristics": []}],
                    "characteristics": [],
                }
            ],
        },
    }
    return input


def test_valid(valid_input):
    result = RigettiProviderProperties.parse_raw_schema(json.dumps(valid_input))
    assert (
        result.braketSchemaHeader.name == "braket.device_schema.rigetti.rigetti_provider_properties"
    )


def test__missing_schemaHeader(valid_input):
    valid_input.pop("braketSchemaHeader")
    with pytest.raises(ValidationError):
        RigettiProviderProperties.parse_raw_schema(json.dumps(valid_input))


def test__missing_specs(valid_input):
    valid_input.pop("specs")
    with pytest.raises(ValidationError):
        RigettiProviderProperties.parse_raw_schema(json.dumps(valid_input))
