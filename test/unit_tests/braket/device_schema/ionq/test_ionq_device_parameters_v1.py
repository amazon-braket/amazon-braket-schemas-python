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


@pytest.mark.parametrize(
    "malicious_type",
    [
        "os.system",
        "subprocess.run",
        "sympy.utilities._compilation.compile_link_import_strings",
        "not_a_real_module.NotARealClass",
        # braket.* gadgets: reachable under the broad braket namespace, but must
        # be rejected since error mitigation is pinned to the
        # braket.device_schema.error_mitigation subtree.
        "braket.schema_common.schema_header.import_module",
        "braket.schema_common.schema_header.ModuleType",
        "braket.device_schema.gate_model_parameters_v1.GateModelParameters",
    ],
)
def test_error_mitigation_rejects_non_braket_type(valid_input, malicious_type):
    valid_input = dict(valid_input)
    valid_input["errorMitigation"] = [{"type": malicious_type}]
    with pytest.raises(ValueError):
        IonqDeviceParameters.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test__missing_schemaHeader(valid_input):
    valid_input.pop("braketSchemaHeader")
    IonqDeviceParameters.parse_raw_schema(json.dumps(valid_input))


@pytest.mark.xfail(raises=ValidationError)
def test__missing_paradigmProperties(valid_input):
    valid_input.pop("paradigmParameters")
    IonqDeviceParameters.parse_raw_schema(json.dumps(valid_input))
