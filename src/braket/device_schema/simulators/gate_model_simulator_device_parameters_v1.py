from pydantic import Field

from braket.device_schema.gate_model_parameters import GateModelParameters
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class GateModelSimulatorDeviceParameters(BraketSchemaBase):
    """
    This defines the parameters common to all the gatemodel devices.

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.simulators.gate_model_simulator_device_parameters",
        ...        "version": "1",
        ...    },
        ...    "paradigmParameters": {"qubitCount": 1},
        ... }
        >>> GateModelSimulatorDeviceParameters.parse_raw(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.simulators.gate_model_simulator_device_parameters", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    paradigmParameters: GateModelParameters
