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

from typing import Dict, List, Union

from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader

# TODO: Replace the calibration data with actual values we receive from the device.


class OqcProviderProperties(BraketSchemaBase):
    """
    This defines the properties common to all the OQC devices.

    Attributes:
        properties (Dict[str, Dict[str, Union[int, List[int]]]]): Basic specifications for
            the device, such as gate fidelities and coherence times.

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.oqc.oqc_provider_properties",
        ...        "version": "1",
        ...    },
        ...    "properties": {
        ...         "one_qubit": {
        ...            "T1": 123,
        ...            "T2": 456,
        ...            "fRO": 789,
        ...            "fRB": 123,
        ...            "EPE": 123,
        ...            "native_gate_fidelities": [1,2,3],
        ...         },
        ...         "two_qubit": {
        ...             "coupling": 123,
        ...             "CLf": 456,
        ...             "ECR_f": 789,
        ...         },
        ...     },
        ...  }
        >>> OqcProviderProperties.parse_raw_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.oqc.oqc_provider_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    properties: Dict[str, Dict[str, Union[int, List[int]]]]
