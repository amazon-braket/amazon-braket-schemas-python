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

import pytest
from pydantic import ValidationError

from braket.schema_common.schema_base import BraketSchemaBase


@pytest.mark.xfail(raises=ValidationError)
def test_missing_properties():
    BraketSchemaBase()


def test_schema_base_correct(braket_schema_header):
    schema = BraketSchemaBase(braketSchemaHeader=braket_schema_header)
    assert schema.braketSchemaHeader == braket_schema_header
    assert BraketSchemaBase.parse_raw(schema.json()) == schema


@pytest.mark.xfail(raises=ValidationError)
def test_header_name_incorrect():
    BraketSchemaBase(braketSchemaHeader=120)
