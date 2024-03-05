from typing import Optional

from pydantic import BaseModel


class PulseFunctionArgument(BaseModel):
    """
    Defines a pulse function argument

    Attributes:
        name: The argument name
        type: The string name of the argument type
        description: Optional description for the argument

    """

    name: str
    type: str
    optional: bool = False
    description: Optional[str]


class PulseFunction(BaseModel):
    """
    Describes a pulse function

    Attributes:
        functionName: The name of the function
        arguments: List of function arguments
        returnType: Return type of the function. If null function has no return value.

    """

    functionName: str
    arguments: list[PulseFunctionArgument]
    returnType: Optional[str]
