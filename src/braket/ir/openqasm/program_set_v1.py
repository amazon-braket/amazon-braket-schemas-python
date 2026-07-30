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

from pydantic.v1 import Field, conlist, validator

from braket.ir.openqasm.program_v1 import Program
from braket.schema_common import BraketSchemaHeader
from braket.schema_common.schema_base import BraketSchemaBase


class ProgramSet(BraketSchemaBase):
    """
    OpenQASM Program Set.

    Attributes:
        braketSchemaHeader (BraketSchemaHeader): Schema header. Users do not need
            to set this value. Only default is allowed.
        programs (list[Program]): The list of programs that will be executed as part of
            the program set.

    Examples:
        >>> ProgramSet(programs=[Program(source="OPENQASM 3.0; input float alpha; qubit[2] q; bit[2] c; rx(alpha) q[0]; h q[0]; cx q[0], q[1]; c = measure q;", inputs={"alpha": [0.0, 3.141516]}), # noqa: E501
        {"source": "OPENQASM 3.0; input angle alpha; input angle beta; qubit[2] q; bit[2] c; rx(alpha * beta) q[0]; c = measure q;", "inputs": {"alpha": [1.0, 2.0], "beta": [3.141516]}}]) # noqa: E501
    """

    _PROGRAM_HEADER = BraketSchemaHeader(name="braket.ir.openqasm.program_set", version="1")
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=True)
    programs: conlist(Program, min_items=1)

    @classmethod
    def _get_and_validate_program_executable_count(cls, program) -> int:
        """
        Returns the number of executables in this program based on the length of
        the inputs' values.

        The Program is executed once using the kth item from each inputs' list.
        If the inputs' lists are unequal lengths, the Program is invalid and
        won't be executed.

        Args:
            program (Program): One Program item from the programs list

        Returns:
            program (Program): The same Program, but the inputs have been
                validated to be correct for a ProgramSet

        Raises:
            ValueError: If inputs aren't lists or have unequal lengths.
        """
        if not program.inputs:
            return 1

        input_lengths = {
            len(value) if isinstance(value, list) else -1
            for value in (program.inputs or {}).values()
        }
        # Check for non-iterable inputs
        if -1 in input_lengths:
            raise ValueError("All Program inputs must be lists when using ProgramSet")

        # Check for uniform length using set size
        if len(input_lengths) > 1:
            raise ValueError("All Program inputs must have the same length when using ProgramSet")

        return input_lengths.pop()

    @validator("programs", each_item=True)
    def validate_program_inputs(cls, program) -> Program:
        """
        Validates program input lists for uniform length and type.

        Args:
            program (Program): One Program item from the programs list.

        Returns:
            program (Program): The same Program, but the inputs have been
                validated to be correct for a ProgramSet

        Raises:
            ValueError: If inputs aren't lists or have unequal lengths.

        Note:
            Used by Pydantic's validation system to ensure:
            1. All inputs are lists
            2. All input lists have equal length
        """
        cls._get_and_validate_program_executable_count(program)
        return program

    @property
    def num_executables_per_program(self) -> list[int]:
        """
        Returns
            num_executables_per_program (list[int]): A list of the number of
                executables for each program in the same order as the programs.

        Raises:
            ValueError: If inputs aren't lists or have unequal lengths.
        """
        return [
            self._get_and_validate_program_executable_count(program) for program in self.programs
        ]

    @property
    def num_executables(self) -> int:
        """
        Returns
            num_executables (int): Number of total program executions

        Raises:
            ValueError: If inputs aren't lists or have unequal lengths.
        """
        return sum(self.num_executables_per_program)

    @property
    def num_programs(self) -> int:
        return len(self.programs)
