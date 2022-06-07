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
from typing import List, Union

from pydantic import BaseModel

from braket.ir.ahs.waveform import Waveform


class PhysicalField(BaseModel):
    """
    Represents the temporal and spatial dependence of a control parameter affecting the atoms

    Attributes:
        sequence: Waveform
        pattern:  Values refer to the pattern at the positions setup.atom_array.sites

    Examples:
        >>> PhysicalField(sequence=Waveform,pattern='uniform')
        >>> PhysicalField(sequence=Waveform,pattern=[0.5, 1.0, 0.5, 0.5, 0.5, 0.5])
    """

    sequence: Waveform
    pattern: Union[str, List[Decimal]]
