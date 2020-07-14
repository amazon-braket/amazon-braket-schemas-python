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

from pydantic import BaseModel

from braket.schema_common.schema_header import BraketSchemaHeader  # noqa: F401
from importlib import import_module

class BraketSchemaBase(BaseModel):
    """
    BraketSchemaBase which includes the schema header and should be the parent class for all schemas

    Attributes:
        braketSchemaHeader (BraketSchemaHeader): schema header
    """

    braketSchemaHeader: BraketSchemaHeader


def import_schema_module(schema: BraketSchemaBase):
    """
    Imports the module that holds the schema given the schema

    Args:
        schema (BraketSchemaBase): the schema

    Returns:
        module of the schema

    Raises:
        ModuleNotFoundError: If the schema module cannot be found according to
        schema header

    Examples:
        >> schema = BraketSchemaBase.parse_raw(json_string)
        >> module = import_schema_module(schema)
        >> module.AnnealingTaskResult.parse_raw(json_string)
    """
    name = schema.braketSchemaHeader.name
    version = schema.braketSchemaHeader.version
    module_name = name + "_v"+version.split('.')[0]
    return import_module(module_name)
