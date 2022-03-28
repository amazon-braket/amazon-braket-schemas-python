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

from typing import Dict, TypeVar, Union

from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader

# TODO: Replace the calibration data with actual values we receive from the device.


OneQubitType = TypeVar("OneQubitType", bound=Dict[str, Union[float, int]])
TwoQubitType = TypeVar("TwoQubitType", bound=Dict[str, Union[Dict[str, int], float]])


class OqcProviderProperties(BraketSchemaBase):
    """
    This defines the properties common to all the OQC devices.

    Attributes:
        properties (Dict[str, Dict[str, Union[OneQubitType, TwoQubitType]]]): Basic
            specifications for the device, such as gate fidelities and coherence times.

    Examples:
        >>> import json
        >>> input_json = {
        ... "braketSchemaHeader": {
        ...     "name": "braket.device_schema.oqc.oqc_provider_properties",
        ...     "version": "1",
        ... },
        ... "properties": {
        ...     "one_qubit": {
        ...         "0": {
        ...             "T1": 28.9,
        ...             "T2": 44.5,
        ...             "fRB": 99.93,
        ...             "fRO": 90.3,
        ...             "qubit": 0
        ...         },
        ...     },
        ...     "two_qubit": {
        ...         "0-1": {
        ...             "coupling": {
        ...                 "control_qubit": 0,
        ...                 "target_qubit": 1
        ...             },
        ...             "fCX": 87.7
        ...         },
        ...     },
        ... },
        ... }
        >>> OqcProviderProperties.parse_raw_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.oqc.oqc_provider_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    properties: Dict[str, Dict[str, Union[OneQubitType, TwoQubitType]]]
