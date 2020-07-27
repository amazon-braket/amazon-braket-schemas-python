from typing import Union

from pydantic import Field

from braket.device_schema.annealing_model_parameters_v1 import AnnealingModelParameters
from braket.device_schema.gate_model_parameters_v1 import GateModelParameters
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DeviceParameters(BraketSchemaBase):
    _PROGRAM_HEADER = BraketSchemaHeader(name="braket.device_schema.device_parameters", version="1")
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    deviceParameters: Union[GateModelParameters, AnnealingModelParameters]
