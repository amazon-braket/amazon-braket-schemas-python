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

import json
import re

from pydantic import BaseModel, ConfigDict

from braket.schema_common.schema_header import BraketSchemaHeader


class BraketSchemaBase(BaseModel):
    """
    BraketSchemaBase which includes the schema header and should be the parent class for all schemas

    Attributes:
        braketSchemaHeader (BraketSchemaHeader): Schema header
    """

    model_config = ConfigDict(populate_by_name=True)

    braketSchemaHeader: BraketSchemaHeader

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
            >> schema = BraketSchemaBase.parse_raw(json_string)
            >> module = import_schema_module(schema)
            >> module.AnnealingTaskResult.parse_raw(json_string)
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
        raw = json.loads(json_str)
        header_raw = raw.get("braketSchemaHeader")
        if not header_raw or not isinstance(header_raw, dict):
            # Will raise ValidationError for missing required field
            return BraketSchemaBase.model_validate(raw)
        try:
            schema_header = BraketSchemaHeader(
                name=header_raw.get("name", ""), version=header_raw.get("version", "")
            )
            module = schema_header.import_schema_module()
        except (ModuleNotFoundError, ValueError, KeyError):
            # Fall back to base validation which will raise appropriate error
            return BraketSchemaBase.model_validate(raw)
        name = schema_header.name
        schema_class = BraketSchemaBase.get_schema_class(module, name)
        return schema_class.model_validate(raw)

    @staticmethod
    def get_schema_class(module, name):
        def capitalize_first_alpha(string):
            return re.sub("([a-z])", lambda x: x.groups()[0].upper(), string, 1)

        class_name = "".join([capitalize_first_alpha(s) for s in name.split(".")[-1].split("_")])
        return getattr(module, class_name)

    # Backward-compatible aliases for downstream code using v1 API
    @classmethod
    def parse_raw(cls, json_str: str, **kwargs) -> BraketSchemaBase:
        """Backward-compatible alias for model_validate_json."""
        return cls.model_validate_json(json_str)

    @classmethod
    def parse_obj(cls, obj: dict, **kwargs) -> BraketSchemaBase:
        """Backward-compatible alias for model_validate."""
        return cls.model_validate(obj)

    def dict(self, **kwargs) -> dict:
        """Backward-compatible alias for model_dump."""
        return self.model_dump(**kwargs)

    def json(self, **kwargs) -> str:
        """Backward-compatible alias for model_dump_json."""
        return self.model_dump_json(**kwargs)

    @classmethod
    def construct(cls, **kwargs):
        """Backward-compatible alias for model_construct."""
        return cls.model_construct(**kwargs)
