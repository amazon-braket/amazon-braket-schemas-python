from pydantic import Field

from braket.device_schema.dwave.dwave_advantage_device_level_parameters_v1 import (
    DwaveAdvantageDeviceLevelParameters,
)
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DwaveAdvantageDeviceParameters(BraketSchemaBase):
    """
    This is the description of the D-Wave parameters

    Attributes:
        providerLevelParameters: Parameters that are specific to D-Wave device.
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.dwave.dwave_advantage_device_parameters", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    deviceLevelParameters: DwaveAdvantageDeviceLevelParameters
