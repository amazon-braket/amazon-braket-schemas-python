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

from braket.device_schema.d_wave_parameters_v1 import DWaveParameters
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class AnnealingModelParameters(BraketSchemaBase):
    """
    This is the schema to validate the parameters provided for d-wave annealing model

    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.annealing_model_parameters", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    dWaveParameters: DWaveParameters
