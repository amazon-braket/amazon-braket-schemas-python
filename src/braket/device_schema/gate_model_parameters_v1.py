from pydantic import BaseModel, Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class GateModelParameters(BraketSchemaBase):
    """
    This defines the parameters common to all the gatemodel devices.

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.gate_model_parameters",
        ...        "version": "1",
        ...    },
        ...    "qubitCount": 1
        ... }
        >>> GateModelParameters.parse_raw_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.gate_model_parameters", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    qubitCount: int = Field(gt=0)
