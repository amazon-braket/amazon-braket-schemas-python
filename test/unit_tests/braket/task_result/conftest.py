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
# language governing permissions and limitations under the License.

import pytest

from braket.ir.ahs import Program as AHSProgram
from braket.ir.annealing import Problem, ProblemType
from braket.ir.blackbird import Program as BlackbirdProgram
from braket.ir.jaqcd import CNot
from braket.ir.jaqcd import Program as JaqcdProgram
from braket.ir.openqasm import Program as OpenQASMProgram
from braket.schema_common.schema_header import BraketSchemaHeader
from braket.task_result import (
    AdditionalMetadata,
    DwaveMetadata,
    DwaveTiming,
    IonQMetadata,
    IqmMetadata,
    NativeQuilMetadata,
    OqcMetadata,
    QueraMetadata,
    RigettiMetadata,
    TaskMetadata,
    XanaduMetadata,
)


@pytest.fixture
def braket_schema_header():
    return BraketSchemaHeader(name="test_schema", version="1.0")


@pytest.fixture
def active_variables():
    return [2, 3, 4]


@pytest.fixture
def compiled_program():
    return "DECLARE ro BIT[2]\n"


@pytest.fixture
def native_quil_metadata():
    return NativeQuilMetadata(
        finalRewiring=[32, 21],
        gateDepth=5,
        gateVolume=6,
        multiQubitGateDepth=1,
        programDuration=300.1,
        programFidelity=0.8989,
        qpuRuntimeEstimation=191.21,
        topologicalSwaps=0,
    )


@pytest.fixture
def xanadu_metadata(compiled_program):
    return XanaduMetadata(compiledProgram=compiled_program)


@pytest.fixture
def ionq_metadata():
    return IonQMetadata(majority={"00": 0.5, "11": 0.5})


@pytest.fixture
def rigetti_metadata(compiled_program, native_quil_metadata):
    return RigettiMetadata(
        compiledProgram=compiled_program, nativeQuilMetadata=native_quil_metadata
    )


@pytest.fixture
def dwave_timing():
    return DwaveTiming(
        qpuSamplingTime=1575,
        qpuAnnealTimePerSample=20,
        qpuReadoutTimePerSample=274,
        qpuAccessTime=10917,
        qpuAccessOverheadTime=3382,
        qpuProgrammingTime=9342,
        qpuDelayTimePerSample=21,
        totalPostProcessingTime=117,
        postProcessingOverheadTime=117,
        totalRealTime=10917,
        runTimeChip=1575,
        annealTimePerRun=20,
        readoutTimePerRun=274,
    )


@pytest.fixture
def dwave_metadata(active_variables, dwave_timing, braket_schema_header):
    return DwaveMetadata(
        activeVariables=active_variables,
        timing=dwave_timing,
    )


@pytest.fixture
def oqc_metadata(compiled_program):
    return OqcMetadata(compiledProgram=compiled_program)


@pytest.fixture
def iqm_metadata(compiled_program):
    return IqmMetadata(compiledProgram=compiled_program)


@pytest.fixture
def quera_metadata():
    return QueraMetadata(numSuccessfulShots=100)


@pytest.fixture
def problem():
    return Problem(
        type=ProblemType.QUBO,
        linear={0: 0.3333, 1: -0.333, 4: -0.333, 5: 0.333},
        quadratic={"0,4": 0.667, "0,5": -1, "1,4": 0.667, "1,5": 0.667},
    )


@pytest.fixture
def additional_metadata_annealing(problem, dwave_metadata):
    return AdditionalMetadata(action=problem, dwaveMetadata=dwave_metadata)


@pytest.fixture
def jacqd_program():
    return JaqcdProgram(instructions=[CNot(control=0, target=1)])


@pytest.fixture
def blackbird_program():
    return BlackbirdProgram(
        source="name StateTeleportation \nversion 1.0 \nCoherent({alpha}) | 0",
    )


@pytest.fixture(params=["shiftingFields", "localDetuning"])
def ahs_program(request):
    return AHSProgram(
        setup={
            "ahs_register": {
                "sites": [
                    [0.0, 0.0],
                    [0.0, 3.0e-6],
                    [0.0, 6.0e-6],
                    [3.0e-6, 0.0],
                    [3.0e-6, 3.0e-6],
                    [3.0e-6, 6.0e-6],
                ],
                "filling": [1, 1, 1, 1, 0, 0],
            }
        },
        hamiltonian={
            "drivingFields": [
                {
                    "amplitude": {
                        "time_series": {
                            "values": [0.0, 2.51327e7, 2.51327e7, 0.0],
                            "times": [0.0, 3.0e-7, 2.7e-6, 3.0e-6],
                        },
                        "pattern": "uniform",
                    },
                    "phase": {
                        "time_series": {"values": [0, 0], "times": [0.0, 3.0e-6]},
                        "pattern": "uniform",
                    },
                    "detuning": {
                        "time_series": {
                            "values": [-1.25664e8, -1.25664e8, 1.25664e8, 1.25664e8],
                            "times": [0.0, 3.0e-7, 2.7e-6, 3.0e-6],
                        },
                        "pattern": "uniform",
                    },
                }
            ],
            request.param: [
                {
                    "magnitude": {
                        "time_series": {"values": [-1.25664e8, 1.25664e8], "times": [0.0, 3.0e-6]},
                        "pattern": [0.5, 1.0, 0.5, 0.5, 0.5, 0.5],
                    }
                }
            ],
        },
    )


@pytest.fixture
def openqasm_program():
    return OpenQASMProgram(source="OPENQASM 3.0; cnot $0, $1;")


@pytest.fixture
def additional_metadata_gate_model(jacqd_program, rigetti_metadata):
    return AdditionalMetadata(action=jacqd_program, rigettiMetadata=rigetti_metadata)


@pytest.fixture
def additional_metadata_photonic_model(blackbird_program, xanadu_metadata):
    return AdditionalMetadata(action=blackbird_program, xanadu_metadata=xanadu_metadata)


@pytest.fixture
def additional_metadata_ahs(ahs_program, quera_metadata):
    return AdditionalMetadata(action=ahs_program, quera_metadata=quera_metadata)


@pytest.fixture
def id():
    return "task_id"


@pytest.fixture
def device_id():
    return "device_id"


@pytest.fixture
def shots():
    return 1000


@pytest.fixture
def task_metadata(id, device_id, shots):
    return TaskMetadata(id=id, deviceId=device_id, shots=shots)


@pytest.fixture
def execution_duration():
    return 100
