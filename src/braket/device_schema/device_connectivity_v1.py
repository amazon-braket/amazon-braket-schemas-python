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


class DeviceConnectivity(BraketSchemaBase):

    """
    This schema defines the common properties that need to be existent if a connection is defined.

    Attributes:

        fullyConnected: If each qubit is connected to all other qubits then it called fully connected.
            true if fully connected else it will be false.

        connectivityGraph: It defines the for each qubit what are the connected qubits.
            For a fullyConnected graph it will be empty since all the qubits are connected to each other


    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {"name": "braket.device_schema.device_connectivity", "version": "1",},
        ...    "fullyConnected": True,
        ...    "connectivityGraph": {"1": ["2", "3"]},
        ... }
        >>> DeviceConnectivity.parse_raw_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.device_connectivity", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    fullyConnected = bool
    connectivityGraph = dict
