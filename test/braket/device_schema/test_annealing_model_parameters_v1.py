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

from braket.device_schema.annealing_model_parameters_v1 import AnnealingModelParameters
from braket.device_schema.dwave_parameters_v1 import DwaveParameters


def test_valid():
    input = (
        '{"braketSchemaHeader": {"name": "braket.device_schema.dwave_parameters", '
        '"version": "1"}} '
    )
    d_wave = DwaveParameters.parse_raw_schema(input)
    input_annealing_model = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.annealing_model_parameters",
            "version": "1",
        },
        "dwaveParameters": json.loads(d_wave.json()),
    }
    result = AnnealingModelParameters.parse_raw_schema(json.dumps(input_annealing_model))
    assert result.dwaveParameters == d_wave


@pytest.mark.xfail(raises=ValidationError)
def test__invalid_attribute():
    input = (
        '{"braketSchemaHeader": {"name": "braket.device_schema.annealing_model_parameters", '
        '"version": "1"}} '
    )
    AnnealingModelParameters.parse_raw_schema(input)
