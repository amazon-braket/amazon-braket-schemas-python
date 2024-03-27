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

from braket.device_schema import GateModelParameters
from braket.device_schema.error_mitigation import Debias
from braket.device_schema.ionq.ionq_device_parameters_v1 import IonqDeviceParameters

PARADIGM = {
    "braketSchemaHeader": {
        "name": "braket.device_schema.gate_model_parameters",
        "version": "1",
    },
    "qubitCount": 1,
}


@pytest.fixture(scope="module")
def valid_input():
    return {
        "braketSchemaHeader": {
            "name": "braket.device_schema.ionq.ionq_device_parameters",
            "version": "1",
        },
        "paradigmParameters": PARADIGM,
    }


def test_valid(valid_input):
    result = IonqDeviceParameters.parse_raw_schema(json.dumps(valid_input))
    assert result.braketSchemaHeader.name == "braket.device_schema.ionq.ionq_device_parameters"
    assert result.errorMitigation is None


def test_error_mitigation(valid_input):
    params = IonqDeviceParameters(paradigmParameters=PARADIGM, errorMitigation=[Debias()])
    em_str = "braket.device_schema.error_mitigation.debias.Debias"
    valid_input["errorMitigation"] = [{"type": em_str}]
    result = IonqDeviceParameters.parse_raw_schema(json.dumps(valid_input))
    assert params.errorMitigation == result.errorMitigation


@pytest.mark.parametrize(
    "extra", ["blah", GateModelParameters.parse_raw_schema(json.dumps(PARADIGM))]
)
def test_invalid_error_mitigation(extra):
    with pytest.raises(ValueError):
        IonqDeviceParameters(paradigmParameters=PARADIGM, errorMitigation=[Debias(), extra])


@pytest.mark.xfail(raises=ValidationError)
def test__missing_schemaHeader(valid_input):
    valid_input.pop("braketSchemaHeader")
    IonqDeviceParameters.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test__missing_paradigmProperties(valid_input):
    valid_input.pop("paradigmParameters")
    IonqDeviceParameters.parse_raw_schema(json.dumps(valid_input))
