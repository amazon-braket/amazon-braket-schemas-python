from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic.v1 import BaseModel, Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class InstructionArgument(BaseModel):
    """
    Defines an Instruction argument

    Attributes:
        name: The argument name
        value: The value of the argument
        type: The string name of the argument's value type
        optional: The boolean to represent if argument is optional or not

    """

    name: str
    value: Any
    type: str
    optional: bool = False


class Instruction(BaseModel):
    """
    Defines a Native Gate Calibration Instruction

    Attributes:
        instructionName: The name of the instruction
        arguments: List of instruction's argument
    """

    name: str
    arguments: Optional[List[InstructionArgument]]


class PulseFunctionArgument(BaseModel):
    """
    Defines a pulse function argument

    Attributes:
        name: The argument name
        value: The value of the argument
        type: The string name of the argument's value type
        optional: The boolean to represent if argumenet is optional or not

    """

    name: str
    value: Any
    type: str
    optional: bool = False


class PulseFunction(BaseModel):
    """
    Defines a pulse function used in native gate calibrations

    Attributes:
        name: The name of the pulse function
        arguments: List of the pulse function's arguments
    """

    name: str
    arguments: List[PulseFunctionArgument]


class NativeGate(BaseModel):
    """
    Defines a native gate

    Attributes:
        name: The name of the native gate
        qubits: The name of qubits that the gate acts on
        arguments: The list of the native gate's argument
        calibrations: List of instructions/pulse functions
    """

    name: str
    qubits: List[str]
    arguments: List[str]
    calibrations: List[Union[Instruction, PulseFunction]]


class TemplateWaveformArgument(BaseModel):
    """
    Defines a template waveform's argument

    Attributes:
        name: The name of the template waveform's argument
        value: The value of the argument
        type: The string name of the argument's value type
        optional: The boolean to represent if argumenet is optional or not
    """

    name: str
    value: Any
    type: str
    optional: bool = False


class Waveform(BaseModel):
    """
    Defines the base type for waveforms

    Attributes:
    waveformId: Id to uniquely identify waveforms
    """

    waveformId: str


class TemplateWaveform(Waveform):
    """
    Defines a template waveform

    Attributes:
        name: The name of the template waveform
        arguments: List of waveform's arguments
    """

    name: str
    arguments: List[TemplateWaveformArgument]


class ArbitraryWaveform(Waveform):
    """
    Defines a arbitrary waveform

    Attributes:
        waveformId: The unique identifier for the waveform
        amplitudes: List of Tuple containg two floats to
            denote the real and imaginary part of a complex number
    """

    amplitudes: List[Tuple[float, float]]


class NativeGateCalibrations(BraketSchemaBase):
    """
    Defines the structure of how native gates will be represented

    Attributes:
        gates: Nested dictionary with an outer and inner key.
        Outer key will be the qubit and inner key will be the gate name.
        waveforms: Dictionary that holds waveform ID as the key and waveform as the value

    Examples:
        >>> input_json = {
        ...         "braketSchemaHeader": {
        ...             "name": "braket.device_schema.pulse.native_gate_calibrations",
        ...             "version": "1",
        ...         },
        ...         "gates":
        ...             {
        ...                 "0": {
        ...                     "rx": [{"name": "rx", "qubits": ["0"], "arguments": ["-1.5707963267948966"], "calibrations": [
        ...                           {"name": "barrier", "arguments": [{"name": "qubit", "value": "0", "type": "string"}]},
        ...                           {"name": "play", "arguments": [{"name": "frame", "value": "q0_rf_frame", "type": "frame"},
        ...                                                          {"name": "waveform", "value": "wf_drag_gaussian_0", "type": "waveform"}]},
        ...                            {"name": "barrier", "arguments": [{"name": "qubit", "value": "0", "type": "string"}]
        ...                        },
        ...                        .
        ...                        .
        ...                  },
        ...                   .
        ...                   .
        ...                   .
        ...         },
        ...         "waveforms": {
        ...             "q0_q1_cz_CZ": {"waveformId": "q0_q1_cz_CZ", "amplitudes": [[0.0, 0.0], [0.0, 0.0], ...]},
        ...             "wf_drag_gaussian_0": {"waveformId": "wf_drag_gaussian_0", "name": "drag_gaussian" , "arguments": [
        ...                                                                 {"name": "length", "value": 6.000000000000001e-08, "type": "float"},
        ...                                                                 {"name": "sigma", "value": 6.369913502160144e-09, "type": "float"},
        ...                                                                 {"name": "amplitude", "value": -0.4549282253548838, "type": "float"},
        ...                                                                 {"name": "beta", "value": 7.494904522022295e-10, "type": "float"}]}
        ...                 .
        ...                 .
        ...                 .
        ...         }
        ...     }
        >>> NativeGateCalibrations.parse_raw_schema(json.dumps(input_json))
    """  # noqa: E501

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.pulse.native_gate_calibrations", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    gates: Dict[str, Dict[str, List[NativeGate]]]
    waveforms: Dict[str, Union[TemplateWaveform, ArbitraryWaveform]]
