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

from braket.device_schema.iqm.iqm_provider_properties_v1 import IqmProviderProperties


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.iqm.iqm_provider_properties",
            "version": "1",
        },
        "properties": {
            "one_qubit": {
                "1": {
                    "T1": 3.943757e-05,
                    "T2": 8.2903e-06,
                    "T2_echo": 1.523113e-05,
                    "fRO": 0.9797,
                    "f1Q_simultaneous_RB": 0.99479,
                }
            },
            "two_qubit": {
                "1-2": {
                    "fCZ": 0.99479,
                    "f2Q_simultaneous_RB_Clifford": 0.9991423,
                }
            },
        },
    }
    return input


def test_valid(valid_input):
    result = IqmProviderProperties.parse_raw_schema(json.dumps(valid_input))
    assert result.braketSchemaHeader.name == "braket.device_schema.iqm.iqm_provider_properties"


@pytest.mark.parametrize("missing_field", ["braketSchemaHeader", "properties"])
def test_missing_field(valid_input, missing_field):
    with pytest.raises(ValidationError):
        valid_input.pop(missing_field)
        IqmProviderProperties.parse_raw_schema(json.dumps(valid_input))
