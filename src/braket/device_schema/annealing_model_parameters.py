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


from pydantic import BaseModel

from braket.device_schema.dwave_parameters import DwaveParameters


class AnnealingModelParameters(BaseModel):
    """
    This class defines the parameters provided for d-wave annealing model

    Attributes:
        dwaveParameters: Parameters used to construct dwave task input

    Examples:
        >>> import json
        >>> input_json = {
        ...     "dwaveParameters": {
        ...         "beta": 1
        ...     }
        ... }
        >>> AnnealingModelParameters.parse_raw(json.dumps(input_json))
    """

    dwaveParameters: DwaveParameters
