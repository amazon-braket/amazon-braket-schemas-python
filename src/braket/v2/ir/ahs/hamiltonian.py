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

from pydantic import BaseModel, ConfigDict, Field

from braket.v2.ir.ahs.driving_field import DrivingField
from braket.v2.ir.ahs.local_detuning import LocalDetuning


class Hamiltonian(BaseModel):
    """
    Specifies the Hamiltonian

    Attributes:
        drivingFields: An externally controlled force
            that drives coherent transitions between selected levels of certain atom types
        localDetuning: An externally controlled polarizing force
            the effect of which is accurately described by a frequency shift of certain levels.

    Examples:
        >>> Hamiltonian(drivingFields=[DrivingField],localDetuning=[LocalDetuning])
    """

    model_config = ConfigDict(populate_by_name=True)

    drivingFields: list[DrivingField]
    localDetuning: list[LocalDetuning] = Field(alias="shiftingFields")

    @property
    def shiftingFields(self) -> list[LocalDetuning]:
        """Deprecated alias for :attr:`localDetuning`."""
        return self.localDetuning

    @shiftingFields.setter
    def shiftingFields(self, value: list[LocalDetuning]) -> None:
        self.localDetuning = value

    @shiftingFields.deleter
    def shiftingFields(self) -> None:
        del self.localDetuning
