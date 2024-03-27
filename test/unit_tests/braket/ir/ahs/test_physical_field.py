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
from pydantic.v1 import ValidationError

from braket.ir.ahs.physical_field import PhysicalField

valid_time_series = {"values": [Decimal(0), Decimal(0)], "times": [Decimal(0.0), Decimal(3.0e-6)]}
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
    physical_field = PhysicalField(time_series=valid_time_series, pattern=valid_pattern_str)
    assert physical_field.time_series == valid_time_series
    assert physical_field.pattern == valid_pattern_str


def test_valid_list_pattern():
    physical_field = PhysicalField(time_series=valid_time_series, pattern=valid_pattern_list)
    assert physical_field.time_series == valid_time_series
    assert physical_field.pattern == valid_pattern_list


@pytest.mark.xfail(raises=ValidationError)
def test__missing_pattern():
    PhysicalField(
        time_series=valid_time_series,
    )


@pytest.mark.xfail(raises=ValidationError)
def test__missing_time_series():
    PhysicalField(
        pattern=valid_pattern_str,
    )
