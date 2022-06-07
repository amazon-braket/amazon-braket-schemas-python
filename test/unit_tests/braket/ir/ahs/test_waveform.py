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

from braket.ir.ahs.waveform import Waveform

valid_values = [Decimal(-1.25664e8), Decimal(1.25664e8)]
valid_times = [Decimal(0.0), Decimal(3.0e-6)]


def test_valid():
    waveform = Waveform(values=valid_values, times=valid_times)
    assert waveform.values == valid_values
    assert waveform.times == valid_times


@pytest.mark.xfail(raises=ValidationError)
def test__missing_values():
    Waveform(
        times=valid_times,
    )


@pytest.mark.xfail(raises=ValidationError)
def test__missing_times():
    Waveform(
        values=valid_values,
    )
