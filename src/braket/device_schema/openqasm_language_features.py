from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ClassicalType(str, Enum):
    """
    int x;
    int[<const integer>] x;

    uint x;
    uint[<const integer>] x;

    float x;
    float[<const integer (system dependent constraints)>] x;

    bit x;
    bit[<const integer>] x;

    bool x;

    array[<classical type>, *dims] x;
    """

    INT = "int"
    UINT = "uint"
    FLOAT = "float"
    BIT = "bit"
    BOOL = "bool"
    ARRAY = "array"


class ClassicalControl(str, Enum):
    """
    if (<condition>) {
        <code block>
    } else {
        <code block>
    }

    for i in <range|discrete set|collectible identifier> {
        <code block>
    }

    while (<condition>) {
        <code block>
    }

    def some_subroutine(<arguments, optional>) {
        <code block>
    }
    some_subroutine(<arguments);

    // my_file.inc contains custom gate definitions, subroutines, etc.
    #include my_file.inc
    """

    IF = "if"
    FOR = "for"
    WHILE = "while"
    SUBROUTINE = "subroutine"
    INCLUDE = "include"


class IndexElement(str, Enum):
    """
    array[int, 5] arr = {0, 1, 2, 3, 4};

    int x = arr[2];                         // 2
    array[int, 2] y = arr[1:2:4];           // {1, 3}
    array[int, 4] z = arr[{3, 4, 1, 0}];    // {3, 4, 1, 0}
    """

    INT = "int"
    RANGE = "range"
    DISCRETE_SET = "discrete_set"


class GateModifier(str, Enum):
    """
    // apply inverse of my_gate to qubit q
    inv @ my_gate q;

    // apply my_gate to qubit q2, controlled by q1
    ctrl @ my_gate q1, q2;
    // apply my_gate to qubit q3 controlled by q1 and q2.
    // can control on any number of qubits this way, and also for negctrl.
    ctrl(2) @ my_gate q1, q2, q3;

    // apply my_gate to qubit q2, inversely controlled by q1
    negctrl @ my_gate q1, q2;

    // apply some power my_gate to qubit q. Can use fractional powers ie for sqrt
    pow(<float|int>) @ my_gate q;
    """

    INV = "inv"
    CTRL = "ctrl"
    NEGCTRL = "negctrl"
    POW = "pow"


class BuiltinFunction(str, Enum):
    """
    <var> = <function name>(<arg(s)>);
    """

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
    """
    Unary prefix, binary infix, and assignment operators.
    """

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
    """
    input float x;
    rx(x) q;

    // output is not currently supported
    """

    INPUT = "input"
    OUTPUT = "output"


class QuantumDirective(str, Enum):
    """
    qubit q;
    qubit[<const integer>] qs;

    gate my_gate(<params, optional>) *qubits {
        <gate def body>
    }

    U(θ, ϕ, λ) q;   // https://openqasm.com/language/gates.html#built-in-gates

    // applies global phase to all qubits in scope, limited if i.e. inside gate definition
    gphase(θ);

    // https://docs.aws.amazon.com/braket/latest/developerguide/braket-constructing-circuit.html#braket-gates   # noqa E501
    <braket builtin gate> q(s);

    // reset and measure not currently fully supported
    """

    QUBIT_DECLARATION = "qubit_declaration"
    GATE_DEF = "gate_def"
    PARAMETERIZED_U = "parameterized_u"
    GPHASE = "gphase"
    BRAKET_GATE = "braket_gate"
    RESET = "reset"
    MEASURE = "measure"


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
