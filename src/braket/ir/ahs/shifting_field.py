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

from pydantic import BaseModel

from braket.ir.ahs.physical_field import PhysicalField


class ShiftingField(BaseModel):
    """
    Specifies the shifting field

    formula:-Delta(t)*Sum_k h_k|r_k><r_k|

    states:
        |r_k> : Rydberg state of atom k.
    other symbols:
        Sum_k : summation over all target atoms.

    Attributes:
        magnitude: PhysicalField (“Delta(t)*delta_s")

    Examples:
        >>> ShiftingField(magnitude=PhysicalField)
    """

    magnitude: PhysicalField
