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
from pydantic.v1 import ValidationError

from braket.ir.blackbird import Program as BlackbirdProgram


@pytest.mark.xfail(raises=ValidationError)
def test_missing_source_property():
    BlackbirdProgram()


def test_blackbird_program():
    source = "testsource"
    program = BlackbirdProgram(source=source)
    assert "braket.ir.blackbird.program" == program.braketSchemaHeader.name
    assert source == program.source


def test_parse_obj():
    source = "testsource"
    program = BlackbirdProgram(source=source)
    assert program == BlackbirdProgram.parse_obj(program.dict())


def test_parse_raw():
    source = "testsource"
    program = BlackbirdProgram(source=source)
    assert program == BlackbirdProgram.parse_raw(program.json())
