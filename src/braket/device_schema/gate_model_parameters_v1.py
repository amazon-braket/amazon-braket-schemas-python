from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class GateModelParameters(BraketSchemaBase):
    """
    This defines the parameters common to all the gatemodel devices.

    Examples:
    {
        "braketSchemaHeader": {
            "name": "braket.device_schema.gate_model_parameters",
            "version": "1"
        }
    }
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.gate_model_parameters", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
