# Copyright 2019-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class IonqProviderProperties(BraketSchemaBase):
    """
    This defines the parameters common to all the Ion-Q devices.

    Attributes:
        target: target for the ionq device
        fidelity: fidelity values for the ionq device
        timing: timing values for the ionq device

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.ionq.ionq_provider_parameters",
        ...        "version": "1",
        ...    },
        ...    "target": "ionq.qpu"
        ... }
        >>> IonqDeviceParameters.parse_raw_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.ionq.ionq_provider_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    target: str
    fidelity: dict
    timing: dict
