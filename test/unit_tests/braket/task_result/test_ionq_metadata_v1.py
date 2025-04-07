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

from braket.task_result import IonQMetadata


def test_no_sharpening():
    metadata = IonQMetadata()
    assert metadata.sharpenedProbabilities is None


def test_sharpening_populated():
    histogram = {"00": 0.5, "11": 0.5}
    metadata = IonQMetadata(sharpenedProbabilities=histogram)
    assert metadata.sharpenedProbabilities == histogram


@pytest.mark.parametrize("histogram", [{"a": 0.5}, {"": 0.5}, {"0000": -0.3}, {"11": 1.4}])
@pytest.mark.xfail(raises=ValidationError)
def test_invalid_sharpened_probabilities_vote(histogram):
    IonQMetadata(sharpenedProbabilities=histogram)


@pytest.mark.xfail(raises=ValidationError)
def test_header_incorrect(braket_schema_header):
    IonQMetadata(braketSchemaHeader=braket_schema_header)
