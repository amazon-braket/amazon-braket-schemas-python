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

from braket.device_schema.xanadu.xanadu_provider_properties_v1 import XanaduProviderProperties


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.xanadu.xanadu_provider_properties",
            "version": "1",
        },
        "loopPhases": [0.06293596790273215, 0.15291642690139806, -1.5957742826142312],
        "schmidtNumber": 1.1240597475954237,
        "commonEfficiency": 0.42871142768980564,
        "loopEfficiencies": [0.9106461685832691, 0.8904556756334581, 0.8518902619448591],
        "squeezingParametersMean": {
            "low": 0.6130577606615072,
            "high": 1.0635796125448667,
            "medium": 0.893051739389763,
        },
        "relativeChannelEfficiencies": [
            0.9305010775397536,
            0.9648681625753431,
            0.9518909571324008,
            0.9486638084844965,
            0.8987246282353925,
            0.9726334999710303,
            0.9489037154275138,
            0.9727238556532112,
            1.0,
            0.973400900408643,
            0.8771940466934924,
            0.9271209514090495,
            0.9595068270114586,
            0.9002874120338067,
            0.911213274548878,
            0.9752842185805198,
        ],
    }
    return input


def test_valid(valid_input):
    result = XanaduProviderProperties.parse_raw_schema(json.dumps(valid_input))
    assert (
        result.braketSchemaHeader.name == "braket.device_schema.xanadu.xanadu_provider_properties"
    )


@pytest.mark.xfail(raises=ValidationError)
def test__missing_schemaHeader(valid_input):
    valid_input.pop("braketSchemaHeader")
    XanaduProviderProperties.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.parametrize(
    "missing_key",
    [
        "loopPhases",
        "schmidtNumber",
        "commonEfficiency",
        "loopEfficiencies",
        "squeezingParametersMean",
        "relativeChannelEfficiencies",
    ],
)
@pytest.mark.xfail(raises=ValidationError)
def test__missing_keys(valid_input, missing_key):
    valid_input.pop(missing_key)
    XanaduProviderProperties.parse_raw_schema(json.dumps(valid_input))
