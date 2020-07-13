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


class BraketSchemaBase(BaseModel):
    """
    BraketSchemaBase which includes the schema header and should be the parent class for all schemas

    Attributes:
        braketSchemaHeader (BraketSchemaHeader): schema header
    """

    braketSchemaHeader: BraketSchemaHeader
