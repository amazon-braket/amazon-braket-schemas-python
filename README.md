**DO NOT SHARE OR TALK ABOUT THE CONTENTS OF THIS LIBRARY per the Amazon Beta NDA you signed.**

Amazon Braket Python IR is an open source library that contains all the intermediate representations (IR) for Amazon Braket quantum tasks and offers serialization and deserialization of those IR payloads. Think of the IR as the contract between the Amazon Braket SDK and Amazon Braket API for quantum programs.

## Installation

### Prerequisites
- Python 3.7+

### Steps
 ```bash
 git clone https://github.com/aws/braket-python-ir.git  --branch stable/latest
 pip install -e braket-python-ir
 ```

 To install test dependencies for running tests locally run:
 ```bash
 pip install -e "braket-python-ir[test]"
 ```

You can check your currently installed version of `braket-python-ir` with `pip show`:

```bash
pip show braket-python-ir
```

or alternatively from within Python:

```
>>> from braket import ir
>>> ir.__version__
```

## Usage
There are currently two types of IR, including jacqd (JsonAwsQuantumCircuitDescription) and annealing. See below for their usage.

**Serializing python structures**
```python
from braket.ir.jaqcd import CNot, H, Program, Expectation
from braket.ir.annealing import Problem, ProblemType

program = Program(instructions=[H(target=0), CNot(control=0, target=1)])
print(program.json(indent=2))

"""
{
  "instructions": [
    {
      "target": 0,
      "type": "h"
    },
    {
      "control": 0,
      "target": 1,
      "type": "cnot"
    }
  ],
  "results": null,
  "basis_rotation_instructions": null
}
"""

program = Program(
    instructions=[H(target=0), CNot(control=0, target=1)],
    results=[Expectation(targets=[0], observable=['x'])],
    basis_rotation_instructions=[H(target=0)]
)
print(program.json(indent=2))

"""
{
  "instructions": [
    {
      "target": 0,
      "type": "h"
    },
    {
      "control": 0,
      "target": 1,
      "type": "cnot"
    }
  ],
  "results": [
    {
      "observable": [
        "x"
      ],
      "targets": [
        0
      ],
      "type": "expectation"
    }
  ],
  "basis_rotation_instructions": [
    {
      "target": 0,
      "type": "h"
    }
  ]
}
"""

problem = Problem(type=ProblemType.QUBO, linear={0: 0.3, 4: -0.3}, quadratic={"0,5": 0.667})
print(problem.json(indent=2))

"""
{
  "type": "QUBO",
  "linear": {0: 0.3, 4: -0.3},
  "quadratic": {"0,5": 0.667}
}
"""
```

**Deserializing into python structures**
```python
from braket.ir.jaqcd import Program
from braket.ir.annealing import Problem

jaqcd_string = """
{
  "instructions": [
    {
      "target": 0,
      "type": "h"
    },
    {
      "control": 0,
      "target": 1,
      "type": "cnot"
    }
  ],
  "results": [
    {
      "observable": [
        "x"
      ],
      "targets": [
        0
      ],
      "type": "expectation"
    }
  ],
  "basis_rotation_instructions": [
    {
      "target": 0,
      "type": "h"
    }
  ]
}
"""

program = Program.parse_raw(jaqcd_string)
print(program)

"""
instructions=[H(target=0, type=<Type.h: 'h'>), CNot(control=0, target=1, type=<Type.cnot: 'cnot'>)] results=[Expectation(observable=['x'], targets=[0], type=<Type.expectation: 'expectation'>)] basis_rotation_instructions=[H(target=0, type=<Type.h: 'h'>)]
"""

annealing_string = """
{
  "type": "QUBO",
  "linear": {0: 0.3, 4: -0.3},
  "quadratic": {"0,5": 0.667}
}
"""

problem = Problem.parse_raw(annealing_string)
print(problem)

"""
type=<ProblemType.QUBO: 'QUBO'>, linear={0: 0.3, 4: -0.3}, quadratic={'0,5': 0.667}
"""

```

## Documentation

First `cd` into the `doc` directory and run:
```bash
make html
```

Then open `BRAKET_IR_ROOT/build/documentation/html/index.html` in a browser to view the docs.

## Testing

Make sure to install test dependencies first:
```bash
pip install -e "braket-python-ir[test]"
```

To run the unit tests:
```bash
tox
```

To run an individual test:
```bash
tox -- -k 'your_test'
```

## License

This project is licensed under the Apache-2.0 License.
