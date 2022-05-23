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

from typing import Dict

from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class PhotonModelParameters(BraketSchemaBase):
    """
    Defines parameters common to all photonic model devices.

    Attributes:
        modes: Number of qubits used by the circuit.
        layout: Template for constructing a valid circuit

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.photon_model_parameters",
        ...        "version": "1",
        ...    },
        ...    "modes": {
        ...         "spatial": 1
        ...     },
        ...     "layout": "name template_borealis\nversion 1.0\nMeasureFock() | 0"
        ... }
        >>> PhotonModelParameters.parse_raw_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.photon_model_parameters", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    modes: Dict[str, float]
    layout: str
