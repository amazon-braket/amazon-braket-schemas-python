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
# language governing permissions and limitations under the License

from __future__ import annotations

import re

from pydantic import BaseModel, field_validator

from braket.v2.schema_common.schema_header import BraketSchemaHeader


class BraketSchemaBase(BaseModel):
    """
    BraketSchemaBase which includes the schema header and should be the parent class for all schemas

    Attributes:
        braketSchemaHeader (BraketSchemaHeader): Schema header
    """

    braketSchemaHeader: BraketSchemaHeader

    @field_validator("braketSchemaHeader")
    @classmethod
    def _validate_braket_schema_header(cls, value: BraketSchemaHeader) -> BraketSchemaHeader:
        """
        Enforces that a provided ``braketSchemaHeader`` matches the fixed header defined
        by the concrete schema class.

        This reproduces the behavior of Pydantic v1's ``Field(const=...)``, which was
        removed in Pydantic v2. Subclasses pin ``braketSchemaHeader`` to a specific
        default header; providing any other value is rejected. The base class itself
        declares no default, so it accepts any header.
        """
        field = cls.model_fields.get("braketSchemaHeader")
        if field is not None and not field.is_required() and value != field.default:
            raise ValueError(f"braketSchemaHeader must be {field.default!r}, but got {value!r}")
        return value

    @staticmethod
    def import_schema_module(schema: BraketSchemaBase):
        """
        Imports the module that holds the schema given the schema

        Args:
            schema (BraketSchemaBase): The schema

        Returns:
            Module of the schema

        Raises:
            ModuleNotFoundError: If the schema module cannot be found according to
            schema header

        Examples:
            >> schema = BraketSchemaBase.model_validate_json(json_string)
            >> module = import_schema_module(schema)
            >> module.AnnealingTaskResult.model_validate_json(json_string)
        """
        return schema.braketSchemaHeader.import_schema_module()

    @staticmethod
    def parse_raw_schema(json_str: str) -> BraketSchemaBase:
        """
        Return schema object given JSON string

        Args:
             json_str (str): The JSON string of the schema

        Returns:
            BraketSchemaBase: The schema object. This can also be an
            instance of a subclass of BraketSchemaBase.
        """
        schema = BraketSchemaBase.model_validate_json(json_str)
        module = BraketSchemaBase.import_schema_module(schema)
        name = schema.braketSchemaHeader.name
        schema_class = BraketSchemaBase.get_schema_class(module, name)
        return schema_class.model_validate_json(json_str)

    @staticmethod
    def get_schema_class(module, name):
        def capitalize_first_alpha(string):
            return re.sub("([a-z])", lambda x: x.groups()[0].upper(), string, 1)

        class_name = "".join([capitalize_first_alpha(s) for s in name.split(".")[-1].split("_")])
        return getattr(module, class_name)
