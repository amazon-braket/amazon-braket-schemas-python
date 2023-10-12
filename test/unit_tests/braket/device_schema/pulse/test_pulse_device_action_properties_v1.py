import json

import pytest
from pydantic.v1 import ValidationError

from braket.device_schema.pulse.pulse_device_action_properties_v1 import PulseDeviceActionProperties


@pytest.fixture(scope="module")
def valid_input():
    input = {
        "braketSchemaHeader": {
            "name": "braket.device_schema.pulse.pulse_device_action_properties",
            "version": "1",
        },
        "supportedQhpTemplateWaveforms": {
            "flat": {
                "functionName": "flat",
                "arguments": [
                    {"name": "duration", "type": "float"},
                    {"name": "iq", "type": "float"},
                    {"name": "scale", "type": "float", "optional": True},
                    {"name": "phase", "type": "float", "optional": True},
                    {"name": "detuning", "type": "float", "optional": True},
                ],
            },
            "boxcar_kernel": {
                "functionName": "boxcar_kernel",
                "arguments": [
                    {"name": "duration", "type": "float"},
                    {"name": "scale", "type": "float", "optional": True},
                    {"name": "phase", "type": "float", "optional": True},
                    {"name": "detuning", "type": "float", "optional": True},
                ],
            },
            "gaussian": {
                "functionName": "gaussian",
                "arguments": [
                    {"name": "duration", "type": "float"},
                    {"name": "t0", "type": "float"},
                    {"name": "fwhm", "type": "float"},
                    {"name": "scale", "type": "float", "optional": True},
                    {"name": "phase", "type": "float", "optional": True},
                    {"name": "detuning", "type": "float", "optional": True},
                ],
            },
            "drag_gaussian": {
                "functionName": "drag_gaussian",
                "arguments": [
                    {"name": "duration", "type": "float"},
                    {"name": "t0", "type": "float"},
                    {"name": "fwhm", "type": "float"},
                    {"name": "anh", "type": "float"},
                    {"name": "alpha", "type": "float"},
                    {"name": "scale", "type": "float", "optional": True},
                    {"name": "phase", "type": "float", "optional": True},
                    {"name": "detuning", "type": "float", "optional": True},
                ],
            },
            "hrm_gaussian": {
                "functionName": "hrm_gaussian",
                "arguments": [
                    {"name": "duration", "type": "float"},
                    {"name": "t0", "type": "float"},
                    {"name": "fwhm", "type": "float"},
                    {"name": "anh", "type": "float"},
                    {"name": "alpha", "type": "float"},
                    {"name": "second_order_hrm_coeff", "type": "float"},
                    {"name": "scale", "type": "float", "optional": True},
                    {"name": "phase", "type": "float", "optional": True},
                    {"name": "detuning", "type": "float", "optional": True},
                ],
            },
            "erf_square": {
                "functionName": "erf_square",
                "arguments": [
                    {"name": "duration", "type": "float"},
                    {"name": "risetime", "type": "float"},
                    {"name": "pad_left", "type": "float"},
                    {"name": "pad_right", "type": "float"},
                    {"name": "scale", "type": "float", "optional": True},
                    {"name": "phase", "type": "float", "optional": True},
                    {"name": "detuning", "type": "float", "optional": True},
                ],
            },
        },
        "ports": {
            "q0_rf": {
                "portId": "q0_rf",
                "direction": "tx",
                "portType": "rf",
                "dt": 1e-9,
            },
            "q1_rf": {
                "portId": "q1_rf",
                "direction": "tx",
                "portType": "rf",
                "dt": 1e-9,
            },
            "q120_ff": {
                "portId": "q120_ff",
                "direction": "tx",
                "portType": "ff",
                "dt": 1e-9,
                "associatedQubits": [120],
                "centerFrequencies": [4.5e9, 4.2e9],
                "qhpSpecificProperties": {"port_detail": "value"},
            },
        },
        "frames": {
            "q0_rf_frame": {
                "frameId": "q0_rf_frame",
                "portId": "q0_rf",
                "frequency": 4525620740.86441,
                "phase": 0.0,
                "centerFrequency": 4500000000.0,
                "qubitMappings": [0],
            },
            "q120_q27_frame": {
                "frameId": "q0_rf_frame",
                "portId": "q0_rf",
                "frequency": 4525620740.86441,
                "phase": 0.0,
                "associatedGate": "xy",
                "qubitMappings": [120, 127],
                "qhpSpecificProperties": {"port_detail": "value"},
            },
        },
        "supportedFunctions": {
            "newframe": {
                "functionName": "newframe",
                "arguments": [
                    {"name": "frame", "type": "frame"},
                    {"name": "frequency", "type": "float"},
                    {"name": "phase", "type": "float", "optional": True},
                ],
            },
            "shift_phase": {
                "functionName": "shift_phase",
                "arguments": [
                    {"name": "phase", "type": "float"},
                    {"name": "frame", "type": "frame"},
                ],
            },
            "set_phase": {
                "functionName": "set_phase",
                "arguments": [
                    {"name": "phase", "type": "float"},
                    {"name": "frame", "type": "frame"},
                ],
            },
            "shift_frequency": {
                "functionName": "shift_frequency",
                "arguments": [
                    {"name": "frequency", "type": "float"},
                    {"name": "frame", "type": "frame"},
                ],
            },
            "set_frequency": {
                "functionName": "set_frequency",
                "arguments": [
                    {"name": "frequency", "type": "float"},
                    {"name": "frame", "type": "frame"},
                ],
            },
            "play": {
                "functionName": "play",
                "arguments": [
                    {"name": "waveform", "type": "waveform"},
                    {"name": "frame", "type": "frame"},
                ],
            },
            "set_scale": {
                "functionName": "set_scale",
                "arguments": [
                    {"name": "scale", "type": "float"},
                    {"name": "frame", "type": "frame"},
                ],
            },
            "capture_v0": {
                "functionName": "capture_v0",
                "arguments": [{"name": "frame", "type": "frame"}],
                "returnType": "bit",
            },
        },
        "supportsNonNativeGatesWithPulses": False,
        "validationParameters": {
            "MAX_SCALE": 1.0,
            "MAX_AMPLITUDE": 1.0,
            "PERMITTED_FREQUENCY_DIFFERENCE": 1.0,
        },
    }
    return input


def test_valid(valid_input):
    result = PulseDeviceActionProperties.parse_raw_schema(json.dumps(valid_input))
    assert (
        result.braketSchemaHeader.name
        == "braket.device_schema.pulse.pulse_device_action_properties"
    )


@pytest.mark.parametrize("missing_field", ["braketSchemaHeader", "ports", "frames"])
def test_missing_field(valid_input, missing_field):
    with pytest.raises(ValidationError):
        valid_input.pop(missing_field)
        PulseDeviceActionProperties.parse_raw_schema(json.dumps(valid_input))
