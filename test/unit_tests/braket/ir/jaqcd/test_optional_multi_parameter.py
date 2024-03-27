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
from pydantic.v1 import ValidationError

from braket.ir.jaqcd.shared_models import OptionalMultiParameter


def test_missing_targets():
    OptionalMultiParameter()


@pytest.mark.xfail(raises=ValidationError)
def test_list_empty_str():
    OptionalMultiParameter(parameters=[""])


def test_different_str_formats():
    OptionalMultiParameter(parameters=["theta_0", "beta", "gamma1", "0"])


def test_empty_list():
    OptionalMultiParameter(parameters=[])
