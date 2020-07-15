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
# language governing permissions and limitations under the License

from pydantic import BaseModel, constr


class BraketSchemaHeader(BaseModel):
    """
    BraketSchemaHeader which dictates the schema and the version.

    Attributes:
        name (str): name of the schema
        version (str): version of the schema

    Examples:
        >>> BraketSchemaHeader(name="braket.task_result.annealing_task_result", version="1.0")
    """

    name: constr(min_length=1)
    version: constr(min_length=1, max_length=50)
