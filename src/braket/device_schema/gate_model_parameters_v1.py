from pydantic import BaseModel, Field


class GateModelParameters(BaseModel):
    """
    This defines the parameters common to all the gatemodel devices.

    Examples:
        >>> import json
        >>> input_json = {
        ...    "qubitCount": 1
        ... }
        >>> GateModelParameters.parse_raw(json.dumps(input_json))
    """

    qubitCount: int = Field(gt=0)
