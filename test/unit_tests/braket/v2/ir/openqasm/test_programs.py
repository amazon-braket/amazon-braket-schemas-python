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
from pydantic import ValidationError

from braket.v2.ir.openqasm.program_v1 import Program
from braket.v2.schema_common.schema_header import BraketSchemaHeader


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
    schema = Program.model_json_schema()
    schema.pop("description", None)
    schema["$defs"]["BraketSchemaHeader"].pop("description", None)
    assert schema == {
        "$defs": {
            "BraketSchemaHeader": {
                "title": "BraketSchemaHeader",
                "type": "object",
                "properties": {
                    "name": {"title": "Name", "type": "string", "minLength": 1},
                    "version": {
                        "title": "Version",
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 50,
                    },
                },
                "required": ["name", "version"],
            }
        },
        "title": "Program",
        "type": "object",
        "properties": {
            "braketSchemaHeader": {
                "$ref": "#/$defs/BraketSchemaHeader",
                "default": {"name": "braket.v2.ir.openqasm.program", "version": "1"},
            },
            "source": {"title": "Source", "type": "string"},
            "inputs": {
                "title": "Inputs",
                "default": None,
                "anyOf": [
                    {
                        "type": "object",
                        "propertyNames": {"minLength": 1},
                        "additionalProperties": {
                            "anyOf": [
                                {"type": "string", "minLength": 1, "pattern": "^[01]+$"},
                                {"type": "number"},
                                {"type": "integer"},
                                {
                                    "type": "array",
                                    "items": {
                                        "anyOf": [
                                            {
                                                "type": "string",
                                                "minLength": 1,
                                                "pattern": "^[01]+$",
                                            },
                                            {"type": "number"},
                                            {"type": "integer"},
                                        ]
                                    },
                                },
                            ]
                        },
                    },
                    {"type": "null"},
                ],
            },
        },
        "required": ["source"],
    }
