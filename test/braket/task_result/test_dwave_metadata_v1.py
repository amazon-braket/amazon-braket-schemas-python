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

import pytest
from pydantic import ValidationError

from braket.task_result.dwave_metadata_v1 import DWaveMetadata, DWaveTiming


@pytest.mark.xfail(raises=ValidationError)
def test_missing_properties(braket_schema_header):
    DWaveMetadata(braketSchemaHeader=braket_schema_header)


def test_dwave_metadata_correct(active_variables, dwave_timing, braket_schema_header):
    metadata = DWaveMetadata(braketSchemaHeader=braket_schema_header, activeVariables=active_variables, timing=dwave_timing)
    assert metadata.activeVariables == active_variables
    assert metadata.timing == dwave_timing
    assert DWaveMetadata.parse_raw(metadata.json()) == metadata


@pytest.mark.parametrize("active_variables", [(23), ([-1])])
@pytest.mark.xfail(raises=ValidationError)
def test_active_variables_incorrect(braket_schema_header, active_variables, dwave_timing):
    DWaveMetadata(braketSchemaHeader=braket_schema_header, activeVariables=active_variables, timing=dwave_timing)


@pytest.mark.xfail(raises=ValidationError)
def test_dwave_timing_incorrect():
    DWaveTiming(
        qpuSamplingTime=-100,
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
