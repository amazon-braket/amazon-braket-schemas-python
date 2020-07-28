from typing import Optional, Union

from pydantic import BaseModel

from braket.device_schema.annealing_model_parameters import AnnealingModelParameters
from braket.device_schema.gate_model_parameters import GateModelParameters


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
        ...     "gateModelParameters": {"qubitCount": 1}
        ... }
        >>> DeviceParameters.parse_raw(json.dumps(gate_model_input_json))
        >>> annealing_model_input_json = {
        ...    "annealingModelParameters": {
        ...        "dwaveParameters": {
        ...             "beta": 1
        ...        },
        ...    },
        ... }
        >>> DeviceParameters.parse_raw(json.dumps(annealing_model_input_json))

    """

    annealingModelParameters: Optional[AnnealingModelParameters]
    gateModelParameters: Optional[GateModelParameters]
