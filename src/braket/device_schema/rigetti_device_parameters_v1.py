from pydantic import Field

from braket.device_schema.gate_model_parameters_v1 import GateModelParameters
from braket.schema_common import BraketSchemaHeader


class RigettiDeviceParameters(GateModelParameters):
    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.rigetti_device_parameters", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    qubitCount: int = Field(gt=0, lt=32)
