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

from typing import Annotated, Optional

from pydantic import Field

from braket.device_schema.dwave.dwave_provider_level_parameters_v1 import ResultFormat
from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class DwaveAdvantageDeviceLevelParameters(BraketSchemaBase):
    """
    This is the description of the D-Wave parameters

    Attributes:
        annealingOffsets (Optional[List[float] = Field(default=None)]): Provides offsets to annealing paths, per qubit.
        annealingSchedule (Optional[List[List[float] = Field(default=None)]]): Introduces variations to the global anneal
            schedule.
        annealingDuration (Optional[int] = Field(default=None) = Field(gt=1)): Sets the duration (in microseconds) of
            quantum annealing time, per read.
        autoScale (Optional[bool] = Field(default=None)): Indicates whether h and J values are rescaled.
        compensateFluxDrift (Optional[bool] = Field(default=None)): Boolean flag indicating whether the D-Wave system
            compensates for flux drift.
        fluxBiases (Optional[List[float] = Field(default=None)]): List of flux-bias offset values with which to calibrate
            a chain. Often required when using the extended J range to create a strongly coupled
            chain for certain embeddings.
        initialState (Optional[List[int] = Field(default=None)]): When using the reverse annealing feature,
            you must supply the initial state to which the system is set.
        maxResults (Optional[int] = Field(default=None) = Field(gt=1)): Specifies the maximum number of
            answers returned from the solver.
        programmingThermalizationDuration (Optional[int] = Field(default=None)): Gives the time (in microseconds) to wait
            after programming the QPU for it to cool back to base temperature (i.e.,
            post-programming thermalization time).
        readoutThermalizationDuration (Optional[int] = Field(default=None)): Gives the time (in microseconds) to wait
            after each state is read from the QPU for it to cool back to base temperature
            (i.e., post-readout thermalization time).
        reduceIntersampleCorrelation (Optional[bool] = Field(default=None)): Reduces sample-to-sample correlations caused
            by the spin-bath polarization effect by adding a delay between reads.
        reinitializeState (Optional[bool] = Field(default=None)): When using the reverse annealing feature,
            you must supply the initial state to which the system is set.
        resultFormat (Optional[ResultFormat] = Field(default=None)): Type of the result format returned by the QPU.
        spinReversalTransformCount (Optional[int] = Field(default=None) = Field(gt=0)): Specifies the number of
            spin-reversal transforms to perform.

    Examples:
        >>> import json
        >>> input_json = {
        ...    "braketSchemaHeader": {
        ...        "name": "braket.device_schema.dwave.dwave_advantage_device_level_parameters",
        ...        "version": "1",
        ...    }
        ... }
        >>> DwaveAdvantageDeviceLevelParameters.model_validate_json_schema(json.dumps(input_json))

    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.dwave.dwave_advantage_device_level_parameters", version="1"
    )
    braketSchemaHeader: Annotated[BraketSchemaHeader, Field(_PROGRAM_HEADER)] = Field(
        default=_PROGRAM_HEADER
    )
    annealingOffsets: Optional[list[float]] = Field(default=None)
    annealingSchedule: Optional[list[list[float]]] = Field(default=None)
    annealingDuration: Optional[float] = Field(default=None, gt=0)
    autoScale: Optional[bool] = Field(default=None)
    compensateFluxDrift: Optional[bool] = Field(default=None)
    fluxBiases: Optional[list[float]] = Field(default=None)
    initialState: Optional[list[int]] = Field(default=None)
    maxResults: Optional[int] = Field(default=None, gt=0)
    programmingThermalizationDuration: Optional[int] = Field(default=None)
    readoutThermalizationDuration: Optional[int] = Field(default=None)
    reduceIntersampleCorrelation: Optional[bool] = Field(default=None)
    reinitializeState: Optional[bool] = Field(default=None)
    resultFormat: Optional[ResultFormat] = Field(default=None)
    spinReversalTransformCount: Optional[int] = Field(default=None, gt=0)
