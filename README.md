**DO NOT SHARE OR TALK ABOUT THE CONTENTS OF THIS LIBRARY per the Amazon Beta NDA you signed.**

Amazon Braket Python IR is an open source library that contains all the intermediate representations (IR) for Amazon Braket quantum tasks and offers serialization and deserialization of those IR payloads. Think of the IR as the contract between the Amazon Braket SDK and Amazon Braket API for quantum programs.

## Installation

### Prerequisites
- Python 3.7+
### Steps
 ```bash
 git clone https://github.com/aws/braket-python-ir.git
 pip install -e braket-python-ir
 ```

 To install test dependencies for running tests locally run:
 ```bash
 pip install -e "braket-python-ir[test]"
 ```

## Usage
There is currently only one kind of IR and that is the JsonAwsQuantumCircuitDescription, jaqcd. See below for it's usage.

**Serializing python structures**
```python
from braket.ir.jaqcd import CNot, H, Program

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
  ]
}
"""
```

**Deserializing into python structures**
```python
from braket.ir.jaqcd import Program

json_string = """
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
  ]
}
"""

program = Program.parse_raw(json_string)
print(program)

"""
instructions=[H(target=0, type=<Type.h: 'h'>), CNot(control=0, target=1, type=<Type.cnot: 'cnot'>)]
"""
```

## Documentation
TODO

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

## Building Sphinx docs
`cd` into the `doc` directory and run:
```bash
make html
```

You can edit the templates for any of the pages in the docs by editing the .rst files in the `doc` directory and then running `make html` again.

## License

This project is licensed under the Apache-2.0 License.
