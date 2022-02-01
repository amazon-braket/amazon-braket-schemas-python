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
from pydantic import ValidationError

from braket.device_schema.oqc.oqc_provider_properties_v1 import OqcProviderProperties


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.oqc.oqc_provider_properties",
            "version": "1",
        },
        "properties": {
            "one_qubit": {
                "T1": 123,
                "T2": 456,
                "fRO": 789,
                "fRB": 123,
                "native-gate-fidelities": [1, 2, 3],
                "EPE": 123,
            },
            "two_qubit": {
                "coupling": 123,
                "CLf": 456,
                "ECR_f": 789,
            },
        },
    }
    return input


def test_valid(valid_input):
    result = OqcProviderProperties.parse_raw_schema(json.dumps(valid_input))
    assert result.braketSchemaHeader.name == "braket.device_schema.oqc.oqc_provider_properties"


@pytest.mark.xfail(raises=ValidationError)
def test__missing_schemaHeader(valid_input):
    valid_input.pop("braketSchemaHeader")
    OqcProviderProperties.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test__missing_specs(valid_input):
    valid_input.pop("properties")
    OqcProviderProperties.parse_raw_schema(json.dumps(valid_input))
