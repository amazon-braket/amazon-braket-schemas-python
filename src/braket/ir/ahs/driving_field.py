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


class DrivingField(BaseModel):
    """
    Specifies the driving field

    formula:((Omega(t)/2)*exp(1j*phi(t))*Sum_k|g_k><r_k|+h.c.)-Delta(t)*Sum_k|r_k><r_k|

    states:
        |g_k> : ground state of atom k.

        |r_k> : Rydberg state of atom k.
    other symbols:
        Sum_k : summation over all target atoms.

        h.c.  : Hermitian conjugate of the preceeding term.

    Attributes:
        amplitude: PhysicalField(pattern=“uniform”) (“Ω(t)”)
        phase: PhysicalField(pattern=“uniform”) (“P(t)”)
        detuning: PhysicalField(pattern=“uniform”) (“D(t)”)

    Examples:
        >>> DrivingField(amplitude=PhysicalField,phase=PhysicalField,detuning=PhysicalField)
    """

    amplitude: PhysicalField
    phase: PhysicalField
    detuning: PhysicalField
