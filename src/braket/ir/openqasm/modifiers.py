from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel


class Control(BaseModel):
    name: str = "ctrl"
    max_qubits: Optional[int] = None  # None indicates no limit


class NegControl(BaseModel):
    name: str = "negctrl"
    max_qubits: Optional[int] = None  # None indicates no limit


class ExponentType(str, Enum):
    INT = "int"
    FLOAT = "float"


class Power(BaseModel):
    name: str = "pow"
    exponent_types: List[ExponentType]


class Inverse(BaseModel):
    name: str = "inv"


Modifier = Union[Control, Power, Inverse]
