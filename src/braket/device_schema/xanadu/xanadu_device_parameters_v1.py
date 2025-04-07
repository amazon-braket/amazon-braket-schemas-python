# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from typing import Annotated

from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class XanaduDeviceParameters(BraketSchemaBase):
    """
    This defines the parameters common to all the Xanadu devices.

    Attributes:
        paradigmParameters: Parameters that are common to photonic devices
        gateParameters: A dictionary of gate parameters to two numbers representing
            the lower and upper bound for each parameter.
        target: Device name
    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.xanadu.xanadu_device_parameters",
        ...        "version": "1",
        ...    },
        ... }
        >>> XanaduDeviceParameters.model_validate_json_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.xanadu.xanadu_device_parameters", version="1"
    )
    braketSchemaHeader: Annotated[BraketSchemaHeader, Field(_PROGRAM_HEADER)] = Field(
        default=_PROGRAM_HEADER
    )
