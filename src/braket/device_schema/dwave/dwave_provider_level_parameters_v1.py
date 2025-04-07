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

from enum import Enum
from typing import Annotated, Optional, Union

from pydantic import Field

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class PostProcessingType(str, Enum):
    """
    The type of processing for D-Wave.
    """

    SAMPLING = "SAMPLING"
    OPTIMIZATION = "OPTIMIZATION"


class ResultFormat(str, Enum):
    """
    The type of results format for D-Wave.
    """

    RAW = "RAW"
    HISTOGRAM = "HISTOGRAM"


class DwaveProviderLevelParameters(BraketSchemaBase):
    """
    This is the description of the D-Wave parameters

    Attributes:
        annealingOffsets (Optional[List[float] = Field(default=None)]): Provides offsets to annealing paths, per qubit.
        annealingSchedule (Optional[List[List[float] = Field(default=None)]]): Introduces variations to the global anneal
            schedule.
        annealingDuration (Optional[int] = Field(default=None) = Field(gt=1)): Sets the duration (in microseconds) of
            quantum annealing time, per read.
        autoScale (Optional[bool] = Field(default=None)): Indicates whether h and J values are rescaled.
        beta (Optional[float] = Field(default=None)): Provides a value for the Boltzmann distribution parameter.
            Used when sampling postprocessing is enabled on D-Wave 2000Q and earlier systems.
        chains (Optional[List[List[int] = Field(default=None)]]): Defines which qubits represent the same logical
            variable. Used only when postprocessing is enabled on D-Wave 2000Q and earlier systems.
            Ensures that all qubits in the same chain have the same value within each sample.
        compensateFluxDrift (Optional[bool] = Field(default=None)): Boolean flag indicating whether the D-Wave system
            compensates for flux drift.
        fluxBiases (Optional[List[float] = Field(default=None)]): List of flux-bias offset values with which to calibrate
            a chain. Often required when using the extended J range to create a strongly coupled
            chain for certain embeddings.
        initialState (Optional[List[int] = Field(default=None)]): When using the reverse annealing feature,
            you must supply the initial state to which the system is set.
        maxResults (Optional[int] = Field(default=None) = Field(gt=1)): Specifies the maximum number of
            answers returned from the solver.
        postprocessingType (Optional[Union[PostProcessingType, str] = Field(default=None)]): Defines what type
             of postprocessing the system runs online on raw solutions.
        postprocessingType (Optional[PostProcessingType] = Field(default=None)): Defines what type of postprocessing the
            system runs online on raw solutions.
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
        ...        "name": "braket.device_schema.dwave.dwave_provider_level_parameters",
        ...        "version": "1",
        ...    },
        ...    "beta": 1
        ... }
        >>> DwaveProviderLevelParameters.model_validate_json_schema(json.dumps(input_json))

    """

    _PROGRAM_HEADER = BraketSchemaHeader(
        name="braket.device_schema.dwave.dwave_provider_level_parameters", version="1"
    )
    braketSchemaHeader: Annotated[BraketSchemaHeader, Field(_PROGRAM_HEADER)] = Field(
        default=_PROGRAM_HEADER
    )
    annealingOffsets: Optional[list[float]] = Field(default=None)
    annealingSchedule: Optional[list[list[float]]] = Field(default=None)
    annealingDuration: Optional[int] = Field(default=None, gt=0)
    autoScale: Optional[bool] = Field(default=None)
    beta: Optional[float] = Field(default=None)
    chains: Optional[list[list[int]]] = Field(default=None)
    compensateFluxDrift: Optional[bool] = Field(default=None)
    fluxBiases: Optional[list[float]] = Field(default=None)
    initialState: Optional[list[int]] = Field(default=None)
    maxResults: Optional[int] = Field(default=None, gt=0)
    postprocessingType: Optional[Union[PostProcessingType, str]] = Field(default=None)
    programmingThermalizationDuration: Optional[int] = Field(default=None)
    readoutThermalizationDuration: Optional[int] = Field(default=None)
    reduceIntersampleCorrelation: Optional[bool] = Field(default=None)
    reinitializeState: Optional[bool] = Field(default=None)
    resultFormat: Optional[ResultFormat] = Field(default=None)
    spinReversalTransformCount: Optional[int] = Field(default=None, gt=0)
