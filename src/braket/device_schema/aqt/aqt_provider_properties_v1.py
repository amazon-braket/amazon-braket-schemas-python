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

from datetime import datetime

from pydantic.v1 import BaseModel, ConfigDict, Field

from braket.schema_common.schema_base import BraketSchemaBase
from braket.schema_common.schema_header import BraketSchemaHeader


class GateFidelity(BaseModel):
    """**Gate fidelity**

    Specifies the gate fidelity with a value between 0 and 100 and an additional
    uncertainty value. The sum of these two values cannot exceed 100.
    """

    value: float = Field(ge=0, le=100)
    uncertainty: float = Field(ge=0, le=100)


class PositiveFloatValueWithUncertainty(BaseModel):
    value: float = Field(gt=0)
    uncertainty: float = Field(ge=0)


mean_two_qubit_gate_fidelity_description = """
<b>The mean two-qubit gate fidelity</b>
<br>
The mean two-qubit gate fidelity is determined following the Randomized
Benchmarking (RB) protocol. To measure the mean error rate we apply a
sequence of randomly chosen gates followed by an inverting gate. The decay
in performance as a function of the sequence length reveals the mean error
rate per gate.
"""

t2_description = """
<b>T2 coherence time (no Spin Echo) in seconds</b>
<br>
The T2 coherence time is estimated by performing Ramsey experiments with a
variable waiting time. The amplitude of the contrast of phase scans of Ramsey
experiments is measured as a function of the waiting time. The coherence is
extracted by measuring the exponential decay of the contrast as a function
of the waiting time.
"""


t1_description = """
<b>T1 in seconds</b>
<br>
Literature value from <a href="https://doi.org/10.1103/PhysRevA.62.032503"
target="_blank">https://doi.org/10.1103/PhysRevA.62.032503</a>.
"""

single_qubit_gate_fidelity_description = """
<b>The single-qubit gate fidelity for each qubit</b>
<br>
A set of key-value pairs, where the key represents the index of the
qubit and the value the fidelity for single-qubit gates.
<br><br>
The single-qubit gate fidelities are determined following the Randomized
Benchmarking (RB) protocol. To measure the mean error rate we apply a
sequence of randomly chosen gates followed by an inverting gate. The decay
in performance as a function of the sequence length reveals the mean error
rate per gate.
"""

spam_fidelity_description = """
<b>SPAM fidelity (lower bound)</b>
<br>
The SPAM fidelity or State Preparation and Measurement errors as the name
indicates describe the errors that occur when the initial quantum state is
not prepared as intended or when the readout of the quantum state yields an
incorrect result. To measure the state preparation errors the qubits are
prepared in a known state followed by a set of repeated measurements that
allow to estimate the probability of correctly preparing and measuring that
given state. To estimate the measurement errors, a known gate is applied
followed by a set of repeated measurements that allow to determine the error
in preparing and measuring incorrectly the final state after that given
operation.
"""

readout_time_description = """
<b>The readout time in microseconds</b>
<br>
The readout time is the duration of the pulse used to detect the ion state.
"""

single_qubit_gate_duration_description = """
Average duration to execute a single-qubit gate in microseconds.
"""

two_qubit_gate_duration_description = """
Average duration to execute a two-qubit gate in microseconds.
"""


class Characterisation(BaseModel):
    """Characterisation data describing a resources properties.

    Attributes:
        single_qubit_gate_fidelity: The single-qubit gate fidelity for each qubit.
        mean_two_qubit_gate_fidelity: The mean two-qubit gate fidelity.
        spam_fidelity_lower_bound: The SPAM fidelity (lower bound).
        t2_coherence_time_s: T2 coherence time (no Spin Echo) in seconds.
        t1_s: T1 in seconds. Literature value from https://doi.org/10.1103/PhysRevA.62.032503.
        readout_time_micros: The duration of detecting the ion state in microseconds.
        single_qubit_gate_duration_micros: Average duration to execute a single-qubit gate in microseconds.
        two_qubit_gate_duration_micros: Average duration to execute a two-qubit gate in microseconds.
        updated_at: Timestamp when this was last updated.
    """

    # Setting the description for the OpenAPI docs explicitly.
    model_config = ConfigDict(
        json_schema_extra={
            "description": "Characterisation data describing a resources properties."
        }
    )

    single_qubit_gate_fidelity: dict[str, GateFidelity] = Field(
        ..., description=single_qubit_gate_fidelity_description
    )
    mean_two_qubit_gate_fidelity: GateFidelity = Field(
        ..., description=mean_two_qubit_gate_fidelity_description
    )
    spam_fidelity_lower_bound: float = Field(
        ..., ge=0, le=100, description=spam_fidelity_description
    )
    t2_coherence_time_s: PositiveFloatValueWithUncertainty = Field(..., description=t2_description)
    t1_s: PositiveFloatValueWithUncertainty = Field(..., description=t1_description)
    readout_time_micros: float = Field(ge=0, description=readout_time_description)
    single_qubit_gate_duration_micros: float = Field(
        ge=0, description=single_qubit_gate_duration_description
    )
    two_qubit_gate_duration_micros: float = Field(
        ge=0, description=two_qubit_gate_duration_description
    )
    updated_at: datetime = Field(..., description="Timestamp when this was last updated")


class AqtProviderProperties(BraketSchemaBase):
    """
    This defines the properties common to all the IQM devices.

    Attributes:
        properties (Dict[str, Dict[str, QubitType]]): Basic specifications for
            the device, such as gate fidelities and coherence times.
    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.aqt.aqt_provider_properties", version="1"
    )
    braketSchemaHeader: BraketSchemaHeader = Field(default=_PROGRAM_HEADER, const=_PROGRAM_HEADER)
    properties: Characterisation
