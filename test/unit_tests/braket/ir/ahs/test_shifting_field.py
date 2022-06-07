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

from braket.ir.ahs.shifting_field import ShiftingField

valid_atom_field = {"sequence": {"values": [], "times": []}, "pattern": ""}


def test_valid():
    shifting_field = ShiftingField(magnitude=valid_atom_field)
    assert shifting_field.magnitude == valid_atom_field


@pytest.mark.xfail(raises=ValidationError)
def test__missing_magnitude():
    ShiftingField()
