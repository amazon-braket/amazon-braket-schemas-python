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

import pytest
from braket.ir.jaqcd import CNot, Program
from pydantic import ValidationError


@pytest.mark.xfail(raises=ValidationError)
def test_missing_instructions_property():
    Program()


@pytest.mark.xfail(raises=ValidationError)
def test_non_instruction():
    Program(instructions=["foo"])


@pytest.mark.xfail(raises=ValidationError)
def test_partial_non_instruction():
    Program(instructions=[CNot(control=0, target=1), "foo"])
