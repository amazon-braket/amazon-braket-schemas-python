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

from importlib import import_module

from pydantic import Field, field_serializer, field_validator

from braket.v2.device_schema.error_mitigation.error_mitigation_properties import (
    ErrorMitigationProperties,
)
from braket.v2.device_schema.error_mitigation.error_mitigation_scheme import ErrorMitigationScheme
from braket.v2.schema_common import BraketSchemaBase, BraketSchemaHeader


class IonqProviderProperties(BraketSchemaBase):
    """
    This defines the properties common to all the IonQ devices.

    Attributes:
        fidelity(dict[str, dict[str, float]]): Average fidelity, the measured success
            to perform operations of the given type.
        timing(dict[str, float]): The timing characteristics of the device. 1Q, 2Q, readout,
            and reset are the operation times. T1 and T2 are decoherence times
        errorMitigation (Optional[dict[Type[ErrorMitigationScheme], ErrorMitigationProperties]]):
            The error mitigation schemes supported by the device, where the key is the Python type
            of the error mitigation scheme and the value contains the properties of the scheme.
            Default: None.

    Examples:
        >>> import json
        >>> input_json = {
        ...     "braketSchemaHeader": {
        ...         "name": "braket.v2.device_schema.ionq.ionq_provider_properties",
        ...         "version": "1",
        ...     },
        ...     "fidelity": {
        ...         "1Q": {
        ...           "mean": 0.99717
        ...         },
        ...         "2Q": {
        ...           "mean": 0.9696
        ...         },
        ...         "spam": {
        ...           "mean": 0.9961
        ...         }
        ...       },
        ...       "timing": {
        ...         "T1": 10000000000,
        ...         "T2": 500000,
        ...         "1Q": 1.1e-05,
        ...         "2Q": 0.00021,
        ...         "readout": 0.000175,
        ...         "reset": 3.5e-05
        ...       },
        ...     errorMitigation: {
        ...         "braket.v2.device_schema.error_mitigation.debias.Debias": {
        ...             "minimumShots": 2500
        ...         }
        ...     }
        ... }
        >>> IonqProviderProperties.parse_raw_schema(json.dumps(input_json))
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.v2.device_schema.ionq.ionq_provider_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER)
    fidelity: dict[str, dict[str, float]]
    timing: dict[str, float]
    errorMitigation: dict[type[ErrorMitigationScheme], ErrorMitigationProperties] | None = None

    @field_validator("errorMitigation", mode="before")
    @classmethod
    def _deserialize_error_mitigation(cls, value):
        """
        Converts the JSON representation of ``errorMitigation`` (where keys are the
        fully-qualified names of the error mitigation scheme classes) into the internal
        representation (where keys are the scheme classes themselves). Keys that are
        already classes are left untouched, so this works for both JSON and Python inputs.
        """
        if not value:
            return value
        deserialized = {}
        for scheme, properties in value.items():
            if isinstance(scheme, str):
                module_name, class_name = scheme.rsplit(".", 1)
                scheme = getattr(import_module(module_name), class_name)
            deserialized[scheme] = properties
        return deserialized

    @field_serializer("errorMitigation", when_used="json")
    def _serialize_error_mitigation(self, value):
        """
        Serializes ``errorMitigation`` for JSON output by replacing the error mitigation
        scheme class keys with their fully-qualified names. Mirrors the deserialization
        performed by :meth:`_deserialize_error_mitigation`.
        """
        if not value:
            return value
        return {
            f"{scheme.__module__}.{scheme.__name__}": (
                properties.model_dump() if hasattr(properties, "model_dump") else properties
            )
            for scheme, properties in value.items()
        }
