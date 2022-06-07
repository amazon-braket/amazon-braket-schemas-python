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

from braket.ir.ahs.atom_array import AtomArray

valid_site_input = [
    [Decimal(0.0), Decimal(0.0)],
    [Decimal(0.0), Decimal(3.0e-6)],
    [Decimal(0.0), Decimal(6.0e-6)],
    [Decimal(3.0e-6), Decimal(0.0)],
    [Decimal(3.0e-6), Decimal(3.0e-6)],
    [Decimal(3.0e-6), Decimal(6.0e-6)],
]
valid_filling = [Decimal(1), Decimal(1), Decimal(1), Decimal(1), Decimal(0), Decimal(0)]


def test_valid():
    atom_array = AtomArray(sites=valid_site_input, filling=valid_filling)
    assert atom_array.sites == valid_site_input
    assert atom_array.filling == valid_filling


@pytest.mark.xfail(raises=ValidationError)
def test__missing_sites():
    AtomArray(
        filling=valid_filling,
    )


@pytest.mark.xfail(raises=ValidationError)
def test__missing_filling():
    AtomArray(
        sites=valid_site_input,
    )
