from typing import Union

from pydantic import BaseModel

from braket.device_schema.annealing_model_parameters_v1 import AnnealingModelParameters
from braket.device_schema.gate_model_parameters_v1 import GateModelParameters


class DeviceParameters(BaseModel):

    """
    This calls defines the parameters that can be provided while creating qunatum tasks
    for any given device

    Attributes:
        deviceParameters: parameters of a device. It has to be either one of GateModelParameters or
            AnnealingModelParameters

    Examples:
        >>> import json
        >>> gate_model_input_json = {
        ...    "deviceParameters": {
        ...        "deviceParameters": {"qubitCount": 1}
        ...    }
        ... }
        >>> DeviceParameters.parse_raw(json.dumps(gate_model_input_json))
        >>> annealing_model_input_json = {
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
        >>> DeviceParameters.parse_raw(json.dumps(annealing_model_input_json))

    """

    deviceParameters: Union[GateModelParameters, AnnealingModelParameters]
