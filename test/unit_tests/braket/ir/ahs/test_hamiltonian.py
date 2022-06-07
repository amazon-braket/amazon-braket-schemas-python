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

from braket.ir.ahs.hamiltonian import Hamiltonian

valid_driving_fields = []
valid_shifting_fields = []


def test_valid():
    hamiltonian_field = Hamiltonian(
        driving_fields=valid_driving_fields, shifting_fields=valid_shifting_fields
    )
    assert hamiltonian_field.driving_fields == valid_driving_fields
    assert hamiltonian_field.shifting_fields == valid_shifting_fields


@pytest.mark.xfail(raises=ValidationError)
def test__missing_driving_fields():
    Hamiltonian(
        shifting_fields=valid_shifting_fields,
    )


@pytest.mark.xfail(raises=ValidationError)
def test__missing_shifting_fields():
    Hamiltonian(
        driving_fields=valid_driving_fields,
    )
