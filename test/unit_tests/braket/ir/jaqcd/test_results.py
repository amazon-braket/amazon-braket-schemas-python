import json

import pytest
from pydantic import ValidationError
from test_common import (
    create_class_instance,
    create_switcher,
    create_valid_class_instance,
    create_valid_json,
    idfn,
)

from braket.ir.jaqcd import Program
from braket.ir.jaqcd.results import (
    Amplitude,
    DensityMatrix,
    Expectation,
    Probability,
    Sample,
    StateVector,
    Variance,
)
from braket.ir.jaqcd.shared_models import MultiState, Observable, OptionalMultiTarget

testdata = [
    (Amplitude, [MultiState], "amplitude"),
    (Expectation, [OptionalMultiTarget, Observable], "expectation"),
    (Sample, [OptionalMultiTarget, Observable], "sample"),
    (Probability, [OptionalMultiTarget], "probability"),
    (StateVector, [], "statevector"),
    (DensityMatrix, [], "densitymatrix"),
    (Variance, [OptionalMultiTarget, Observable], "variance"),
]


@pytest.mark.parametrize("testclass,subclasses,type", testdata, ids=idfn)
def test_subclass(testclass, subclasses, type):
    for subclass in subclasses:
        assert issubclass(testclass, subclass)


@pytest.mark.parametrize("testclass,subclasses,type", testdata, ids=idfn)
@pytest.mark.xfail(raises=ValidationError)
def test_invalid_type(testclass, subclasses, type):
    switcher = create_switcher(type="gobbledygook")
    create_class_instance(switcher, testclass, subclasses)


@pytest.mark.parametrize("testclass,subclasses,type", testdata, ids=idfn)
def test_valid_json(testclass, subclasses, type):
    json_obj = create_valid_json(subclasses, type)
    json_raw = json.dumps(json_obj)
    result = create_valid_class_instance(testclass, subclasses, type)
    assert json.loads(result.json()) == json_obj
    assert testclass.parse_raw(json_raw) == result


@pytest.mark.parametrize("testclass,subclasses,type", testdata, ids=idfn)
def test_result_in_program(testclass, subclasses, type):
    result = create_valid_class_instance(testclass, subclasses, type)
    program = Program(instructions=[], results=[result])
    assert program.results == [result]
