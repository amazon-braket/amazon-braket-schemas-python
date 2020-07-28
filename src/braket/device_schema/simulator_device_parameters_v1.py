from pydantic import Field

from braket.device_schema.gate_model_parameters_v1 import GateModelParameters
from braket.schema_common import BraketSchemaHeader


class SimulatorDeviceParameters(GateModelParameters):

    """
    This defines the schema for parameters that will be provided as part of create quantum task
    for a simulator

    Attributes:
        qubitCount: the qubit count of the task. It should be greater than 0 and
            less than 31[simulators only supports 30 qubits]

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.simulator_device_parameters",
        ...        "version": "1"
        ...    },
        ...    "qubitCount": 30
        ... }
        >>> SimulatorDeviceParameters.parse_raw_schema(json.dumps(input_json))

    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.simulator_device_parameters", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    qubitCount: int = Field(gt=0, lt=31)
