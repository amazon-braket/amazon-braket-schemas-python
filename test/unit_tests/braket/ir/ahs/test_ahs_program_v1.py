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
from pydantic import ValidationError

from braket.ir.ahs.program_v1 import Program

valid_setup_input = {
    "atom_array": {
        "sites": [
            [0.0, 0.0],
            [0.0, 3.0e-6],
            [0.0, 6.0e-6],
            [3.0e-6, 0.0],
            [3.0e-6, 3.0e-6],
            [3.0e-6, 6.0e-6],
        ],
        "filling": [1, 1, 1, 1, 0, 0],
    }
}

valid_hamiltonian_input = {
    "driving_fields": [
        {
            "amplitude": {
                "sequence": {
                    "values": [0.0, 2.51327e7, 2.51327e7, 0.0],
                    "times": [0.0, 3.0e-7, 2.7e-6, 3.0e-6],
                },
                "pattern": "uniform",
            },
            "phase": {
                "sequence": {"values": [0, 0], "times": [0.0, 3.0e-6]},
                "pattern": "uniform",
            },
            "detuning": {
                "sequence": {
                    "values": [-1.25664e8, -1.25664e8, 1.25664e8, 1.25664e8],
                    "times": [0.0, 3.0e-7, 2.7e-6, 3.0e-6],
                },
                "pattern": "uniform",
            },
        }
    ],
    "shifting_fields": [
        {
            "magnitude": {
                "sequence": {"values": [-1.25664e8, 1.25664e8], "times": [0.0, 3.0e-6]},
                "pattern": [0.5, 1.0, 0.5, 0.5, 0.5, 0.5],
            }
        }
    ],
}


def test_valid():
    program = Program(
        setup=valid_setup_input,
        hamiltonian=valid_hamiltonian_input,
    )
    assert Program.parse_raw_schema(program.json()) == program
    assert program == Program.parse_raw_schema(program.json())


@pytest.mark.xfail(raises=ValidationError)
def test__missing_setup():
    Program(
        hamiltonian=valid_hamiltonian_input,
    )


@pytest.mark.xfail(raises=ValidationError)
def test__missing_hamiltonian():
    Program(
        setup=valid_setup_input,
    )
