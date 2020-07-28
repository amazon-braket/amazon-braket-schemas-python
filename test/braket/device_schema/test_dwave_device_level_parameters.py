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

import json

import pytest
from pydantic import ValidationError

from braket.device_schema.dwave_device_level_parameters import DwaveDeviceLevelParameters


def test_valid():
    input = {}
    assert DwaveDeviceLevelParameters.parse_raw(json.dumps(input))


@pytest.mark.xfail(raises=ValidationError)
def test_invalid_attribute():
    input = '{"annealingOffsets": 1}'
    # annealingOffsets should be List[int]
    DwaveDeviceLevelParameters.parse_raw(input)
