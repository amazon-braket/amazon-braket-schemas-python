from pydantic import Field

from braket.device_schema.dwave.dwave_device_level_parameters_v1 import DwaveDeviceLevelParameters
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
        ...         "name": "braket.device_schema.dwave.dwave_device_parameters",
        ...         "version": "1",},
        ...     "deviceLevelParameters": {
        ...         "braketSchemaHeader": {
        ...             "name": "braket.device_schema.dwave.dwave_device_level_parameters",
        ...             "version": "1",
        ...     },}
        ... }
        >>> DwaveDeviceParameters.parse_raw_schema(json.dumps(input_json))

    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.dwave.dwave_device_parameters", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    deviceLevelParameters: DwaveDeviceLevelParameters
