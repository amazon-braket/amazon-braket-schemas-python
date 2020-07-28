from typing import List, Optional

from braket.device_schema.device_action_properties import DeviceActionProperties
from braket.ir.jaqcd.program_v1 import GateInstructions, Results


class JaqcdDeviceActionProperties(DeviceActionProperties):

    """
    This defines the schema for properties for the actions that can be supported by the
        jaqcd devices

    Attributes:
        supportedOperations: operations supported by the jaqcd action
        supportedResultTypes: result types that are supported by the jaqcd action.

    Examples:
        >>> import json
        >>> input_json = {
        ...    "actionType": "braket.ir.jaqcd.program",
        ...    "version": ["1.0", "1.1"],
        ...    "supportedOperations": [{"control": 0, "target": 1, "type": "cnot"}],
        ...    "supportedResultTypes": [{"observable": ["x"], "targets": [1], "type": "expectation"}],
        ... }
        >>> JaqcdDeviceActionProperties.parse_raw(json.dumps(input_json))

    """

    supportedOperations: List[GateInstructions]
    supportedResultTypes: Optional[List[Results]]
