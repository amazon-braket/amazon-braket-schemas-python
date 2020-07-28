from pydantic import Field

from braket.device_schema.dwave_device_level_parameters import DwaveDeviceLevelParameters
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DwaveDeviceParameters(BraketSchemaBase):
    """
    This is the description of the d-wave parameters

    Attributes:
        deviceLevelParameters: Parameters that are specific to dwave device.
    
    Examples:
        >>> import json
        >>> input_json = {
        ...     "braketSchemaHeader": {
        ...         "name": "braket.device_schema.dwave_device_properties",
        ...         "version": "1",},
        ...     "deviceLevelParameters": {}
        ... }
        >>> DwaveDeviceParameters.parse_raw(json.dumps(input_json))

    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.dwave_device_parameters", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    deviceLevelParameters: DwaveDeviceLevelParameters
