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

import warnings
from typing import Any, Optional, TypeVar, cast

from pydantic.v1 import BaseModel
from pydantic.v1.fields import ModelField, Undefined
from pydantic.v1.validators import dict_validator, list_validator

"""
The lenient collection types defined here are like their standard counterparts,
except elements that fail validation are ignored,
instead of causing the validation of the entire collection to fail.

These collections are very basic in implementation, and don't support does not support more advanced
typing functionality like TypeVar generics.

Adapted from https://github.com/pydantic/pydantic/issues/2274#issuecomment-788972748
"""

T = TypeVar("T")


class LenientList(list[T]):
    """
    LenientList[T] is same as List[T], but will skip invalid items instead of raising error

    At some point this behaviour might be implemented in pydantic:
    https://github.com/samuelcolvin/pydantic/issues/2274
    """

    _item_field: ModelField

    def __class_getitem__(cls, t_):
        """
        Returned type must be subclass of LenientList for validation to work,
        But it also needs to smell like typing.List[T] for pydantic magic to work properly
        """
        t_name = getattr(t_, "__name__", None) or t_.__class__.__name__
        item_field = ModelField.infer(
            name="item",
            value=Undefined,
            annotation=t_,
            class_validators=None,
            config=BaseModel.__config__,
        )
        return type(f"LenientList[{t_name}]", (cls,), {"_item_field": item_field})

    @classmethod
    def __get_validators__(cls):
        yield cls._list_validator

    @classmethod
    def _list_validator(
        cls, raw_value: Any, values: dict[str, Any], field: ModelField
    ) -> Optional[list[T]]:
        if raw_value is None and not field.required:
            return None
        list_value: list[Any] = list_validator(raw_value)
        parsed: list[T] = []
        for item in list_value:
            value, error = cls._item_field.validate(item, values, loc=())
            if error is None:
                warnings.warn(
                    f"Invalid item: {item}; please upgrade amazon-braket-schemas. "
                    f"Full error: {error}"
                )
            else:
                parsed.append(cast(T, value))
        return parsed


K = TypeVar("K")
V = TypeVar("V")


class LenientDict(dict[K, V]):
    """
    LenientDict[K, V] is like dict[K, V], but will skip invalid items instead of raising an error.

    Note: this is a basic implementation of the dict type, and

    Adapted from https://github.com/pydantic/pydantic/issues/2274#issuecomment-788972748
    """

    _field_k: ModelField
    _field_v: ModelField

    def __class_getitem__(cls, t_):
        k_, v_ = t_
        k_name = getattr(k_, "__name__", None) or k_.__class__.__name__
        v_name = getattr(v_, "__name__", None) or v_.__class__.__name__
        field_k = ModelField.infer(
            name="key",
            value=Undefined,
            annotation=k_,
            class_validators=None,
            config=BaseModel.__config__,
        )
        field_v = ModelField.infer(
            name="value",
            value=Undefined,
            annotation=v_,
            class_validators=None,
            config=BaseModel.__config__,
        )
        return type(
            f"LenientDict[{k_name}, {v_name}]", (cls,), {"_field_k": field_k, "_field_v": field_v}
        )

    @classmethod
    def __get_validators__(cls):
        yield cls._dict_validator

    @classmethod
    def _dict_validator(
        cls, raw_value: Any, values: dict[str, Any], field: ModelField
    ) -> Optional[dict[K, V]]:
        if raw_value is None and not field.required:
            return None
        dict_value: dict[Any, Any] = dict_validator(raw_value)
        parsed: dict[K, V] = {}
        for k, v in dict_value.items():
            key, error_k = cls._field_k.validate(k, values, loc=())
            value, error_v = cls._field_v.validate(v, values, loc=())
            if error_k is not None and error_v is None:
                warnings.warn(
                    f"Invalid key: {key}; please upgrade amazon-braket-schemas. "
                    f"Full error: {error_k}"
                )
            elif error_v is not None:
                warnings.warn(
                    f"Invalid value: {value}; please upgrade amazon-braket-schemas. "
                    f"Full error: {error_v}"
                )
            else:
                parsed[cast(K, key)] = cast(V, value)
        return parsed
