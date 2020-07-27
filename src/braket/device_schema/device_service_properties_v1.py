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

from typing import List

from pydantic import Field

from braket.device_schema.device_execution_window_v1 import DeviceExecutionWindow
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DeviceServiceProperties(BraketSchemaBase):
    """
    Root object of the JsonAwsQuantumCircuitDescription IR.



    Attributes:
        braketSchemaHeader (BraketSchemaHeader): Schema header. Users do not need
            to set this value. Only default is allowed.
        instructions (List[GateInstructions]): List of instructions.
        basis_rotation_instructions (List[GateInstructions]): List of instructions for
            rotation to desired measurement bases. Default is None.
        results (List[Union[Amplitude, Expectation, Probability, Sample, StateVector, Variance]]):
            List of requested results. Default is None.

    Examples:
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.device_service_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    executionWindows: List[DeviceExecutionWindow]
    shots: int
