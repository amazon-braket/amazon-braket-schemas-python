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

import pytest
from pydantic.v1 import ValidationError

from braket.schema_common.schema_header import BraketSchemaHeader, import_braket_module


@pytest.fixture
def name():
    return "braket.test.schema"


@pytest.fixture
def version():
    return "1.0"


@pytest.mark.xfail(raises=ValidationError)
def test_missing_properties():
    BraketSchemaHeader()


def test_schema_header_correct(name, version):
    header = BraketSchemaHeader(name=name, version=version)
    assert header.name == name
    assert header.version == version
    assert BraketSchemaHeader.parse_raw(header.json()) == header


@pytest.mark.xfail(raises=ValidationError)
def test_header_name_incorrect(version):
    BraketSchemaHeader(name="", version=version)


@pytest.mark.xfail(raises=ValidationError)
def test_header_version_incorrect(name):
    BraketSchemaHeader(name=name, version="")


@pytest.mark.parametrize(
    "version",
    [
        "1; rm -rf /",
        "1.0.dev0",
        "latest",
        "../../etc/passwd",
        "1 ",
    ],
)
def test_header_version_rejects_non_numeric(name, version):
    with pytest.raises(ValidationError):
        BraketSchemaHeader(name=name, version=version)


def test_import_braket_module_imports_braket_module():
    module = import_braket_module("braket.schema_common.schema_header")
    assert module.import_braket_module is import_braket_module


@pytest.mark.parametrize(
    "module_name",
    [
        "os",
        "os.path",
        "subprocess",
        "sympy.utilities._compilation",
        "not_braket.something",
        "braketfoo",
    ],
)
def test_import_braket_module_rejects_non_braket_namespace(module_name):
    with pytest.raises(ValueError, match="is not in the 'braket' namespace"):
        import_braket_module(module_name)


def test_import_braket_module_respects_narrow_namespace():
    namespace = "braket.device_schema.error_mitigation"
    module = import_braket_module(f"{namespace}.debias", namespace=namespace)
    from braket.device_schema.error_mitigation import debias

    assert module is debias


@pytest.mark.parametrize(
    "module_name",
    [
        # reachable under braket. but outside the error_mitigation subtree:
        # the gadgets the broad-prefix check would have allowed.
        "braket.schema_common.schema_header",
        "braket.device_schema.gate_model_parameters_v1",
        "braket",
    ],
)
def test_import_braket_module_rejects_outside_narrow_namespace(module_name):
    namespace = "braket.device_schema.error_mitigation"
    with pytest.raises(ValueError, match=f"is not in the '{namespace}' namespace"):
        import_braket_module(module_name, namespace=namespace)
