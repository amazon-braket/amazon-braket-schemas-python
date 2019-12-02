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

from pydantic import BaseModel, confloat, conint, conlist


class SingleTarget(BaseModel):
    """
    Single target index.

    Attributes:
        target (int): The target index. This is an int >= 0.

    Examples:
        >>> SingleTarget(target=0)
    """

    target: conint(ge=0)


class DoubleTarget(BaseModel):
    """
    Target indices of length 2.

    Attributes:
        targets (List[int]): A list with two items and all items are int >= 0.

    Examples:
        >>> DoubleTarget(targets=[0, 1])
    """

    targets: conlist(conint(ge=0), min_items=2, max_items=2)


class MultiTarget(BaseModel):
    """
    Variable length target indices.

    Attributes:
        targets (List[int]): A list with at least two items and all items are int >= 0.

    Examples:
        >>> MultiTarget(targets=[0, 1])
    """

    targets: conlist(conint(ge=0), min_items=2)


class MultiControl(BaseModel):
    """
    Variable length control indices.

    Attributes:
        controls (List[int]): A list with at least two items and all items are int >= 0.

    Examples:
        >>> MultiControl(controls=[0, 1])
    """

    controls: conlist(conint(ge=0), min_items=2)


class DoubleControl(BaseModel):
    """
    Control indices of length 2.

    Attributes:
        controls (List[int]): A list with two items and all items are int >= 0.

    Examples:
        >>> DoubleControl(targets=[0, 1])
    """

    controls: conlist(conint(ge=0), min_items=2, max_items=2)


class SingleControl(BaseModel):
    """
    Single control index.

    Attributes:
        control (int): The control index. This is an int >= 0.

    Examples:
        >>> SingleControl(control=0)
    """

    control: conint(ge=0)


class Angle(BaseModel):
    """
    Single angle in radians (floating point).

    Attributes:
        angle (float): The angle in radians.
            inf, -inf, and NaN are not allowable inputs.

    Examples:
        >>> Angle(angle=0.15)
    """

    angle: confloat(gt=float("-inf"), lt=float("inf"))
