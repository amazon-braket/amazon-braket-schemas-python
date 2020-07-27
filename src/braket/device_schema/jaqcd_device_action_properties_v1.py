from typing import List, Optional

from pydantic import Field

from braket.device_schema.device_action_properties_v1 import DeviceActionProperties
from braket.ir.jaqcd.program_v1 import GateInstructions, Results
from braket.schema_common import BraketSchemaHeader


class JaqcdDeviceActionProperties(DeviceActionProperties):

    """
    This defines the schema for properties for the actions that can be supported by the
        jaqcd devices

    Attributes:
    supportedOperations: operations supported by the jaqcd action
    supportedResultTypes: result types that are supported by the jaqcd action.

    Examples:
    {
        "braketSchemaHeader": {
            "name": "braket.device_schema.jaqcd_device_action_properties",
            "version": "1",
        },
        "actionType": "braket.ir.jaqcd.program",
        "version": ["1.0", "1.1"],
        "supportedOperations": [{"control": 0, "target": 1, "type": "cnot"}],
        "supportedResultTypes": [{"observable": ["x"], "targets": [1], "type": "expectation"}],
    }
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.jaqcd_device_action_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    supportedOperations: List[GateInstructions]
    supportedResultTypes: Optional[List[Results]]
