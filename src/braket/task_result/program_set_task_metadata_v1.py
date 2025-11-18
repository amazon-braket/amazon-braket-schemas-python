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
# language governing permissions and limitations under the License

from typing import Optional, Union

from pydantic.v1 import BaseModel, Field, conint, constr

from braket.device_schema.common.gate_model_device_parameters_v1 import GateModelDeviceParameters
from braket.device_schema.ionq.ionq_device_parameters_v1 import IonqDeviceParameters
from braket.device_schema.iqm.iqm_device_parameters_v1 import IqmDeviceParameters
from braket.device_schema.rigetti.rigetti_device_parameters_v1 import RigettiDeviceParameters
from braket.device_schema.simulators.gate_model_simulator_device_parameters_v1 import (
    GateModelSimulatorDeviceParameters,
)
from braket.schema_common.schema_base import BraketSchemaBase
from braket.schema_common.schema_header import BraketSchemaHeader
from braket.task_result.program_set_executable_cancellation_v1 import (
    ProgramSetExecutableCancellationMetadata,
)
from braket.task_result.program_set_executable_failure_v1 import ProgramSetExecutableFailureMetadata
from braket.task_result.program_set_executable_result_v1 import ProgramSetExecutableResultMetadata


class ProgramMetadata(BaseModel):
    """
    Metadata about the program

    Attributes:
        executables (list[Union[ProgramSetExecutableFailureMetadata,
            ProgramSetExecutableResultMetadata, ProgramSetExecutableCancellationMetadata]]):
            The parameter-injected programs associated
            with this program source
    """

    executables: list[
        Union[
            ProgramSetExecutableFailureMetadata,
            ProgramSetExecutableResultMetadata,
            ProgramSetExecutableCancellationMetadata,
        ]
    ]


class ProgramSetTaskMetadata(BraketSchemaBase):
    """
    The program set task metadata schema.

    Attributes:
        id (str): The ID of the task. For AWS tasks, this is the task ARN.
        requestedShots (int): The total number of shots for each executable.
        successfulShots (int): The total number of shots across all completed executables
        programMetadata (list[ProgramMetadata]): The metadata of the source program
        deviceId (str): The ID of the device on which the task ran.
            For AWS devices, this is the device ARN.
        deviceParameters (Union[GateModelSimulatorDeviceParameters, IonqDeviceParameters,
                            IqmDeviceParameters, RigettiDeviceParameters]):
            The device parameters of the task. Default is None.
        createdAt (str): The timestamp of task creation in ISO-8601/RFC3339 string format
            (YYYY-MM-DDTHH:mm:ss.sssZ)
        endedAt (str): The timestamp of when the task ended in ISO-8601/RFC3339 string format
            (YYYY-MM-DDTHH:mm:ss.sssZ). Default is None.
        status (str): The status of the task. Default is None.
        totalFailedExecutables (int): The number of failed executables in the batch.
    """

    _PROGRAM_SET_TASK_METADATA_HEADER = BraketSchemaHeader(
        name="braket.task_result.program_set_task_metadata", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(
        default=_PROGRAM_SET_TASK_METADATA_HEADER, const=_PROGRAM_SET_TASK_METADATA_HEADER
    )

    id: constr(min_length=1)
    deviceId: constr(min_length=1)
    requestedShots: conint(ge=0)
    successfulShots: conint(ge=0)
    programMetadata: list[ProgramMetadata]
    deviceParameters: Optional[
        Union[
            GateModelSimulatorDeviceParameters,
            IonqDeviceParameters,
            IqmDeviceParameters,
            RigettiDeviceParameters,
            GateModelDeviceParameters,
        ]
    ]
    createdAt: Optional[constr(min_length=1, max_length=24)]
    endedAt: Optional[constr(min_length=1, max_length=24)]
    status: Optional[constr(min_length=1, max_length=20)]
    totalFailedExecutables: int
