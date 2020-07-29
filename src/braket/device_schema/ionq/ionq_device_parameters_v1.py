from pydantic import Field

from braket.device_schema.gate_model_parameters_v1 import GateModelParameters
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class IonqDeviceParameters(BraketSchemaBase):
    """
    This defines the parameters common to all the gatemodel devices.

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.ionq.ionq_device_parameters",
        ...        "version": "1",
        ...    },
        ...    "paradigmParameters": {"braketSchemaHeader": {
        ...        "name": "braket.device_schema.gate_model_parameters",
        ...        "version": "1",
        ...    },"qubitCount": 1},
        ... }
        >>> IonqDeviceParameters.parse_raw_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.ionq.ionq_device_parameters", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    paradigmParameters: GateModelParameters
