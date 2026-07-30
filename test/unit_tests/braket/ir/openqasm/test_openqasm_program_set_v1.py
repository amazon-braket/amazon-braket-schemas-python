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

import json

import pytest
from pydantic.v1 import ValidationError

from braket.ir.openqasm.program_set_v1 import ProgramSet
from braket.ir.openqasm.program_v1 import Program
from braket.schema_common import BraketSchemaHeader


@pytest.mark.parametrize(
    "default_shots, programs",
    [
        (0, [Program(source="")]),
        (0, [Program(source="", inputs={})]),
        (100, [Program(source="", inputs={})]),
        (0, [Program(source="", inputs={"alpha": [0.1, 0.2]})]),
        (0, [Program(source="", inputs={"alpha": []})]),
        (
            0,
            [
                Program(
                    source="OPENQASM 3.0; qubit[2] q; bit[2] c; h q[0]; cx q[0], q[1]; c = measure q;",  # noqa: E501
                    inputs={"alpha": [0.1, 0.2]},
                )
            ],
        ),
        (
            0,
            [
                Program(
                    source="OPENQASM 3.0; input angle alpha; input angle beta; qubit[2] q; bit[2] c; h q[0]; rx(alpha) q[0]; rz(beta) q[1]; cx q[0], q[1]; c = measure q;",  # noqa: E501
                    inputs={"alpha": [0.1, 0.2], "beta": [0.3, 0.4]},
                )
            ],
        ),
        (
            0,
            [
                Program(
                    source="OPENQASM 3.0; input angle alpha; input angle beta; qubit[2] q; bit[2] c; h q[0]; rx(alpha) q[0]; rz(beta) q[1]; cx q[0], q[1]; c = measure q;",  # noqa: E501
                    inputs={"alpha": [0.1, 0.2], "beta": [0.3, 0.4]},
                ),
                Program(
                    source="OPENQASM 3.0; input angle alpha; input angle beta; rx(alpha * beta) $0; c = measure $0;",  # noqa: E501
                    inputs={"alpha": [1.0, 2.0], "beta": [3.0, 4.0]},
                ),
            ],
        ),
        (
            0,
            [
                Program(
                    source="OPENQASM 3.0; ..",
                    inputs={"alpha": [0.1, 0.2], "beta": [0.3, 0.4]},
                ),
                Program(source="OPENQASM 3.0; .."),
            ],
        ),
        (
            0,
            [
                Program(
                    source="OPENQASM 3.0; ..",
                    inputs={"alpha": ["1", "0"], "beta": ["0", "1"]},
                ),
                Program(
                    source="OPENQASM 3.0; ..",
                    inputs={"alpha": ["1"]},
                ),
            ],
        ),
    ],
)
def test_program_set(default_shots, programs):
    ProgramSet(programs=programs)


@pytest.mark.parametrize(
    "programs, value_error_message",
    [
        (
            [
                Program(
                    source="OPENQASM 3.0; ..",
                    inputs={"alpha": 0.1},
                )
            ],
            "All Program inputs must be lists when using ProgramSet",
        ),
        (
            [
                Program(
                    source="OPENQASM 3.0; ..",
                    inputs={"alpha": "0"},
                )
            ],
            "All Program inputs must be lists when using ProgramSet",
        ),
        (
            [
                Program(
                    source="OPENQASM 3.0; ..",
                    inputs={"alpha": [0.1, 0.2], "beta": [0.3]},
                )
            ],
            "All Program inputs must have the same length when using ProgramSet",
        ),
        (
            [
                Program(
                    source="OPENQASM 3.0; ..",
                    inputs={"alpha": [0.1, 0.2], "beta": ["1"]},
                )
            ],
            "All Program inputs must have the same length when using ProgramSet",
        ),
    ],
)
def test_program_set_invalid_program_inputs(programs, value_error_message):
    with pytest.raises(ValueError) as error:
        ProgramSet(programs=programs)
    assert value_error_message in str(error.value)


def test_load_program_set():
    valid_action = json.dumps(
        {
            "braketSchemaHeader": {"name": "braket.ir.openqasm.program_set", "version": "1"},
            "programs": [
                {
                    "source": "OPENQASM 3.0;\nqubit[1] q;\nrx(a+b) q[0];",
                    "inputs": {"a": [3.14, 1.23], "b": [1.02, 2.23]},
                },
                {
                    "source": "OPENQASM 3.0;\nqubit[1] q;\nrx(alpha+beta*gamma) q[0];",
                    "inputs": {"alpha": [0.12], "beta": [0], "gamma": [3.1415926]},
                },
            ],
        }
    )
    program_set = ProgramSet.parse_raw_schema(valid_action)
    assert program_set.num_executables == 3
    assert program_set.num_executables_per_program == [2, 1]
    assert program_set.num_programs == len(program_set.programs) == 2


def test_json_schema():
    schema = ProgramSet.schema()
    schema["properties"]["braketSchemaHeader"].pop("default", None)
    schema.pop("description", None)
    schema["definitions"]["Program"].pop("description", None)
    assert schema == {
        "title": "ProgramSet",
        "type": "object",
        "properties": {
            "braketSchemaHeader": {
                "title": "Braketschemaheader",
                "const": BraketSchemaHeader(name="braket.ir.openqasm.program_set", version="1"),
            },
            "programs": {
                "title": "Programs",
                "type": "array",
                "items": {"$ref": "#/definitions/Program"},
                "minItems": 1,
            },
        },
        "required": ["programs"],
        "definitions": {
            "Program": {
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
                },
                "required": ["source"],
            }
        },
    }


def test_empty():
    with pytest.raises(ValidationError):
        ProgramSet(programs=[])
