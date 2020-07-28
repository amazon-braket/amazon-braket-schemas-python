from typing import Union

from pydantic import Field

from braket.device_schema.annealing_model_parameters_v1 import AnnealingModelParameters
from braket.device_schema.gate_model_parameters_v1 import GateModelParameters
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DeviceParameters(BraketSchemaBase):

    """
    This calls defines the parameters that can be provided while creating qunatum tasks
    for any given device

    Attributes:
        deviceParameters: parameters of a device. It has to be either one of GateModelParameters or
            AnnealingModelParameters

    Examples:
        >>> import json
        >>> gate_model_input_json = {
        ...    "braketSchemaHeader": {"name": "braket.device_schema.device_parameters", "version": "1",},
        ...    "deviceParameters": {
        ...        "braketSchemaHeader": {
        ...            "name": "braket.device_schema.gate_model_parameters",
        ...            "version": "1",
        ...        }
        ...    },
        ... }
        >>> DeviceParameters.parse_raw_schema(json.dumps(gate_model_input_json))
        >>> annealing_model_input_json = {
        ...    "braketSchemaHeader": {"name": "braket.device_schema.device_parameters", "version": "1",},
        ...    "deviceParameters": {
        ...        "braketSchemaHeader": {
        ...            "name": "braket.device_schema.annealing_model_parameters",
        ...            "version": "1",
        ...        },
        ...        "dwaveParameters": {
        ...            "braketSchemaHeader": {
        ...                "name": "braket.device_schema.dwave_parameters",
        ...                "version": "1",
        ...            }
        ...        },
        ...    },
        ... }
        >>> DeviceParameters.parse_raw_schema(json.dumps(annealing_model_input_json))

    """

    _PROGRAM_HEADER = BraketSchemaHeader(name="braket.device_schema.device_parameters", version="1")
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    deviceParameters: Union[GateModelParameters, AnnealingModelParameters]
