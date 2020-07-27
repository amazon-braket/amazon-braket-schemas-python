from typing import Dict, List, Optional, Union

from pydantic import Field

from braket.device_schema.device_action_properties_v1 import DeviceActionProperties
from braket.ir.jaqcd.program_v1 import GateInstructions, Results
from braket.schema_common import BraketSchemaHeader


class JaqcdDeviceActionProperties(DeviceActionProperties):
    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.jaqcd_device_action_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    supportedOperations: List[GateInstructions]
    supportedResultTypes: Optional[List[Results]]
