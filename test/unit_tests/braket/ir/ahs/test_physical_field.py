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

from decimal import Decimal

import pytest
from pydantic import ValidationError

from braket.ir.ahs.physical_field import PhysicalField

valid_sequence = {"values": [Decimal(0), Decimal(0)], "times": [Decimal(0.0), Decimal(3.0e-6)]}
valid_pattern_str = "uniform"
valid_pattern_list = [
    Decimal(0.5),
    Decimal(1.0),
    Decimal(0.5),
    Decimal(0.5),
    Decimal(0.5),
    Decimal(0.5),
]


def test_valid_default_pattern():
    physical_field = PhysicalField(sequence=valid_sequence, pattern=valid_pattern_str)
    assert physical_field.sequence == valid_sequence
    assert physical_field.pattern == valid_pattern_str


def test_valid_list_pattern():
    physical_field = PhysicalField(sequence=valid_sequence, pattern=valid_pattern_list)
    assert physical_field.sequence == valid_sequence
    assert physical_field.pattern == valid_pattern_list


@pytest.mark.xfail(raises=ValidationError)
def test__missing_pattern():
    PhysicalField(
        sequence=valid_sequence,
    )


@pytest.mark.xfail(raises=ValidationError)
def test__missing_sequence():
    PhysicalField(
        pattern=valid_pattern_str,
    )
