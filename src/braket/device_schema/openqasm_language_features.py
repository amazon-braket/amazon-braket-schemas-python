from enum import Enum
from typing import Dict, Optional, List

from pydantic import BaseModel


class ClassicalType(str, Enum):
    INT = "int"
    UINT = "uint"
    FLOAT = "float"
    BIT = "bit"
    BOOL = "bool"


class ClassicalControl(str, Enum):
    IF = "if"
    FOR = "for"
    WHILE = "while"
    SUBROUTINE = "subroutine"


class IndexElement(str, Enum):
    INT = "int"
    RANGE = "range"
    DISCRETE_SET = "discrete_set"


class GateModifier(str, Enum):
    INV = "inv"
    CTRL = "ctrl"
    NEGCTRL = "negctrl"
    POW = "pow"


class BuiltinFunction(str, Enum):
    ARCCOS = "arccos"
    ARCSIN = "arcsin"
    ARCTAN = "arctan"
    CEILING = "ceiling"
    COS = "cos"
    EXP = "exp"
    FLOOR = "floor"
    LOG = "log"
    MOD = "mod"
    POPCOUNT = "popcount"
    POW = "pow"
    ROTL = "rotl"
    ROTR = "rotr"
    SIN = "sin"
    SIZEOF = "sizeof"
    SQRT = "sqrt"
    TAN = "tan"


class BuiltinOperator(str, Enum):
    NOT = "~"
    LOGICAL_NOT = "!"
    MINUS = "-"
    GT = ">"
    LT = "<"
    GE = ">="
    LE = "<="
    EQ = "=="
    NEQ = "!="
    LOGICAL_AND = "&&"
    LOGICAL_OR = "||"
    OR = "|"
    XOR = "^"
    AND = "&"
    LSHIFT = "<<"
    RSHIFT = ">>"
    PLUS = "+"
    MULT = "*"
    DIV = "/"
    MOD = "%"
    POW = "**"
    ASSIGN = "="
    PLUS_EQ = "+="
    MINUS_EQ = "-="
    MULT_EQ = "*="
    DIV_EQ = "/="
    AND_EQ = "&="
    OR_EQ = "|="
    NOT_EQ = "~="
    XOR_EQ = "^="
    LSHIFT_EQ = "<<="
    RSHIFT_EQ = ">>="
    MOD_EQ = "%="
    POW_EQ = "**="


class IODirective(str, Enum):
    INPUT = "input"
    OUTPUT = "output"


class QuantumDirective(str, Enum):
    GATE_DEF = "gate_def"
    PARAMETERIZED_U = "parameterized_u"
    GPHASE = "gphase"
    BRAKET_GATE = "braket_gate"
    RESET = "reset"
    MEASURE = "measure"
    QUBIT_DECLARATION = "qubit_declaration"


class OpenQASMLanguageFeatures(BaseModel):
    """
    Examples:
    >>> import json
    >>> input_json = {
    ...    "classicalVariables": [
    ...         "int",
    ...         "uint",
    ...         "float",
    ...         "bit",
    ...         "bool",
    ...     ],
    ...    "classicalControl": [
    ...         "if",
    ...         "for",
    ...         "while",
    ...         "subroutine",
    ...     ],
    ...    "indexElements": [
    ...         "int",
    ...         "range",
    ...         "discrete_set",
    ...     ],
    ...    "gateModifiers": [
    ...         "inv",
    ...         "ctrl",
    ...         "negctrl",
    ...         "pow",
    ...     ],
    ...    "builtinFunctions": [
    ...         "sin",
    ...         "cos",
    ...         "tan",
    ...         "exp",
    ...     ],
    ...    "builtinOperators": [
    ...         "+", "-", "*", "/", "=", "+=", "-=", "*=", "/=",
    ...     ],
    ...    "ioDirectives": [
    ...         "input",
    ...         "output",
    ...     ],
    ...    "quantumDirectives": [
    ...         "gate_def",
    ...         "parameterized_u",
    ...         "gphase",
    ...         "braket_gate",
    ...         "reset",
    ...         "measure",
    ...         "qubit_declaration",
    ...     ],
    ... }
    >>> OpenQASMLanguageFeatures.parse_raw(json.dumps(input_json))
    """
    classicalVariables: Optional[List[ClassicalType]]
    classicalControl: Optional[List[ClassicalControl]]
    indexElements: Optional[List[IndexElement]]
    gateModifiers: Optional[List[GateModifier]]
    builtinFunctions: Optional[List[BuiltinFunction]]
    builtinOperators: Optional[List[BuiltinOperator]]
    ioDirectives: Optional[List[IODirective]]
    quantumDirectives: Optional[List[QuantumDirective]]
