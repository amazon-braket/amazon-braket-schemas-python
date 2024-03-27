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

from braket.ir.jaqcd.shared_models import Observable


@pytest.mark.xfail(raises=ValidationError)
def test_missing_observable():
    Observable()


@pytest.mark.xfail(raises=ValidationError)
def test_list_partial_non_str():
    Observable(observable=[0, "x"])


@pytest.mark.xfail(raises=ValidationError)
def test_list_non_matching_regex():
    Observable(observable=["fooy"])


@pytest.mark.xfail(raises=ValidationError)
def test_list_partial_non_matching_regex():
    Observable(observable=["fooh", "h"])


@pytest.mark.xfail(raises=ValidationError)
def test_list_partial_non_int():
    Observable(observable=[[0, "foo"]])


@pytest.mark.xfail(raises=ValidationError)
def test_empty_nested_list():
    Observable(observable=[[]])


@pytest.mark.xfail(raises=ValidationError)
def test_element_list_size_gt_two():
    Observable(observable=[[[0, 1, 2]]])


@pytest.mark.xfail(raises=ValidationError)
def test_empty_list():
    Observable(observable=[])


def test_list_matching_regex():
    observable = ["x", "y"]
    obj = Observable(observable=observable)
    assert obj.observable == observable


@pytest.mark.parametrize(
    "observable",
    [
        "2*x",
        "2 * x",
        "20.10 * x",
        "2 * x @ y",
        "2 * x @ y @ z",
        "2 * x @ - 2 * y @ z",
        "2 * x @ y - z @ i",
        "2 * x @ y + 3.1 * z @ i",
        "2 * x @ y - 3.1 * z @ i + h@h",
        "-2 * x @ y + 3.1 * z @ i + h@h",
    ],
)
def test_hamiltonian_regex(observable):
    obj = Observable(observable=observable)
    assert obj.observable == observable


def test_list_2d_matrix():
    observable = [[[[1.0, 0], [0, 1]], [[0.0, 1], [1, 0]]]]
    obj = Observable(observable=observable)
    assert obj.observable == observable


def test_list_extra_params():
    Observable(observable=["x", "y"], foo="bar")
