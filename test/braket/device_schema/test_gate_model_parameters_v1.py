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

from braket.device_schema.gate_model_parameters_v1 import GateModelParameters


def test_valid():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.gate_model_parameters",
            "version": "1",
        },
        "qubitCount": 1,
    }
    result = GateModelParameters.parse_raw_schema(json.dumps(input))
    assert result.qubitCount == 1


@pytest.mark.xfail(raises=ValidationError)
def test__missing_header():
    input = "{} "
    assert GateModelParameters.parse_raw_schema(input)
