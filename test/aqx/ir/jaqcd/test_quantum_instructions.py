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

import json

import pytest
from aqx.ir.jaqcd import (
    CY,
    CZ,
    XX,
    YY,
    ZZ,
    CCNot,
    CNot,
    CPhaseShift,
    CPhaseShift00,
    CPhaseShift01,
    CPhaseShift10,
    CSwap,
    H,
    I,
    ISwap,
    PhaseShift,
    Program,
    PSwap,
    Rx,
    Ry,
    Rz,
    S,
    Si,
    Swap,
    T,
    Ti,
    V,
    Vi,
    X,
    Y,
    Z,
)
from aqx.ir.jaqcd.shared_models import (
    Angle,
    DoubleControl,
    DoubleTarget,
    SingleControl,
    SingleTarget,
)
from pydantic import ValidationError

testdata = [
    (H, [SingleTarget], "h"),
    (I, [SingleTarget], "i"),
    (CNot, [SingleTarget, SingleControl], "cnot"),
    (CCNot, [SingleTarget, DoubleControl], "ccnot"),
    (Rx, [SingleTarget, Angle], "rx"),
    (Ry, [SingleTarget, Angle], "ry"),
    (Rz, [SingleTarget, Angle], "rz"),
    (X, [SingleTarget], "x"),
    (Y, [SingleTarget], "y"),
    (Z, [SingleTarget], "z"),
    (S, [SingleTarget], "s"),
    (Si, [SingleTarget], "si"),
    (T, [SingleTarget], "t"),
    (Ti, [SingleTarget], "ti"),
    (Swap, [DoubleTarget], "swap"),
    (CSwap, [SingleControl, DoubleTarget], "cswap"),
    (ISwap, [DoubleTarget], "iswap"),
    (PSwap, [DoubleTarget, Angle], "pswap"),
    (PhaseShift, [SingleTarget, Angle], "phaseshift"),
    (CPhaseShift, [SingleControl, SingleTarget, Angle], "cphaseshift"),
    (CPhaseShift00, [SingleControl, SingleTarget, Angle], "cphaseshift00"),
    (CPhaseShift01, [SingleControl, SingleTarget, Angle], "cphaseshift01"),
    (CPhaseShift10, [SingleControl, SingleTarget, Angle], "cphaseshift10"),
    (CY, [SingleTarget, SingleControl], "cy"),
    (CZ, [SingleTarget, SingleControl], "cz"),
    (V, [SingleTarget], "v"),
    (Vi, [SingleTarget], "vi"),
    (XX, [DoubleTarget, Angle], "xx"),
    (YY, [DoubleTarget, Angle], "yy"),
    (ZZ, [DoubleTarget, Angle], "zz"),
]


def idfn(val):
    if isinstance(val, list):
        return "_".join([item.__name__ for item in val])
    elif hasattr(val, __name__):
        return val.__name__
    else:
        return str(val)


def single_target_valid_input():
    return {"target": 0}


def two_target_valid_input():
    return {"targets": [0, 1]}


def multi_target_valid_input():
    return {"targets": [0, 1, 2]}


def angle_valid_input():
    return {"angle": 0.123}


def single_control_valid_input():
    return {"control": 0}


def two_control_valid_input():
    return {"controls": [0, 1]}


def multi_control_valid_input():
    return {"controls": [0, 1, 2]}


def type_invalid_input():
    return {"type": "gobbledygook"}


def create_class_instance(switcher, testclass, subclasses):
    input = create_json(switcher, subclasses)
    return testclass(**input)


def create_json(switcher, subclasses):
    input = {}
    for subclass in subclasses:
        input.update(switcher.get(subclass.__name__, lambda: "Invalid subclass")())
    input.update(switcher.get("Type")())
    return input


def create_valid_json(subclasses, type):
    def type_valid_input():
        return {"type": type}

    switcher = {
        "SingleTarget": single_target_valid_input,
        "DoubleTarget": two_target_valid_input,
        "MultiTarget": multi_target_valid_input,
        "Angle": angle_valid_input,
        "SingleControl": single_control_valid_input,
        "DoubleControl": two_control_valid_input,
        "MultiControl": multi_control_valid_input,
        "Type": type_valid_input,
    }
    return create_json(switcher, subclasses)


def create_valid_class_instance(testclass, subclasses, type):
    input = create_valid_json(subclasses, type)
    return testclass(**input)


@pytest.mark.parametrize("testclass,subclasses,type", testdata, ids=idfn)
def test_subclass(testclass, subclasses, type):
    for subclass in subclasses:
        assert issubclass(testclass, subclass)


@pytest.mark.parametrize("testclass,subclasses,type", testdata, ids=idfn)
@pytest.mark.xfail(raises=ValidationError)
def test_invalid_type(testclass, subclasses, type):
    switcher = {
        "SingleTarget": single_target_valid_input,
        "DoubleTarget": two_target_valid_input,
        "MultiTarget": multi_target_valid_input,
        "Angle": angle_valid_input,
        "SingleControl": single_control_valid_input,
        "DoubleControl": two_control_valid_input,
        "MultiControl": multi_control_valid_input,
        "Type": type_invalid_input,
    }
    create_class_instance(switcher, testclass, subclasses)


@pytest.mark.parametrize("testclass,subclasses,type", testdata, ids=idfn)
def test_valid_json(testclass, subclasses, type):
    json_obj = create_valid_json(subclasses, type)
    json_raw = json.dumps(json_obj)
    instruction = create_valid_class_instance(testclass, subclasses, type)
    assert json.loads(instruction.json()) == json_obj
    assert testclass.parse_raw(json_raw) == instruction


@pytest.mark.parametrize("testclass,subclasses,type", testdata, ids=idfn)
def test_instruction_in_program(testclass, subclasses, type):
    instruction = create_valid_class_instance(testclass, subclasses, type)
    program = Program(instructions=[instruction])
    assert program.instructions == [instruction]


# CNOT extra tests


def test_cnot_string_type():
    cnot = CNot(type=CNot.Type.cnot, control=0, target=1)
    assert cnot.type == CNot.Type.cnot


def test_cnot_enum_type():
    cnot = CNot(type="cnot", control=0, target=1)
    assert cnot.type == CNot.Type.cnot


def test_cnot_getters():
    control = 0
    target = 2
    cnot = CNot(control=control, target=target)

    assert cnot.control == control
    assert cnot.target == target
    assert cnot.type == CNot.Type.cnot


# H extra tests


def test_h_string_type():
    h = H(type=H.Type.h, target=0)
    assert h.type == H.Type.h


def test_h_enum_type():
    h = H(type="h", target=0)
    assert h.type == H.Type.h


def test_h_getters():
    target = 0
    h = H(target=target)

    assert h.target == target
    assert h.type == H.Type.h


# Rz extra tests


def test_rz_string_type():
    rz = Rz(type=Rz.Type.rz, target=0, angle=0.15)
    assert rz.type == Rz.Type.rz


def test_rz_enum_type():
    rz = Rz(type="rz", target=0, angle=0.15)
    assert rz.type == Rz.Type.rz


def test_rz_getters():
    target = 0
    rotation = 0.15
    rz = Rz(target=target, angle=rotation)

    assert rz.target == target
    assert rz.type == Rz.Type.rz
