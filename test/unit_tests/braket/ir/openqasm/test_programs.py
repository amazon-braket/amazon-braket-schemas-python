# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
# # or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import pytest
from pydantic.v1.error_wrappers import ValidationError

from braket.ir.openqasm.program_v1 import Program
from braket.schema_common.schema_header import BraketSchemaHeader


def test_empty_programs_without_inputs():
    Program(source="OPENQASM 3.0; h $0; cx $0, $1;")


def test_empty_programs_with_none_inputs():
    Program(source="OPENQASM 3.0; h $0; cx $0, $1;", inputs=None)


def test_empty_programs_with_empty_inputs():
    Program(source="OPENQASM 3.0; h $0; cx $0, $1;", inputs={})


def test_programs_with_inputs():
    Program(
        source="OPENQASM 3.0; rx(alpha * beta) $0; h $0; cx $0, $1;",
        inputs={"alpha": [3.14159, 2.71828, 1.618], "beta": [1.618, 2.71828, 3.14159]},
    )


@pytest.mark.parametrize(
    "inputs",
    [
        {
            "input_1": [3.14159, "abc"],
        },
        {
            "input_1": [float("nan")],
        },
    ],
)
@pytest.mark.xfail(raises=ValidationError)
def test_openqasm_program_set_with_invalid_input_value_should_raise_validation_error(inputs):
    Program(source="", inputs=inputs)


def test_json_schema():
    schema = Program.schema()
    schema.pop("description", None)
    assert schema == {
        "title": "Program",
        "type": "object",
        "properties": {
            "braketSchemaHeader": {
                "title": "Braketschemaheader",
                "default": {"name": "braket.ir.openqasm.program", "version": "1"},
                "const": BraketSchemaHeader(name="braket.ir.openqasm.program", version="1"),
            },
            "source": {"title": "Source", "type": "string"},
            "inputs": {
                "title": "Inputs",
                "type": "object",
                "additionalProperties": {
                    "anyOf": [
                        {"type": "string", "minLength": 1, "pattern": "^[01]+$"},
                        {"type": "number"},
                        {"type": "integer"},
                        {
                            "type": "array",
                            "items": {
                                "anyOf": [
                                    {"type": "string", "minLength": 1, "pattern": "^[01]+$"},
                                    {"type": "number"},
                                    {"type": "integer"},
                                ]
                            },
                        },
                    ]
                },
            },
        },
        "required": ["source"],
    }
