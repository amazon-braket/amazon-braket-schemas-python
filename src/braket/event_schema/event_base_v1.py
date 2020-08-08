# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

import abc
from datetime import datetime
from typing import List

from pydantic import BaseModel, constr
from typing_extensions import Literal


class BraketBaseEvent(BaseModel, abc.ABC):
    """
    The schema for metadata associated with a particular event

    Attributes:
        detailType (str): The type of event
        resources (List[str]): The resources associated with the event
        account (str): The account for which this event was generated
        source (str): The source of the event
        time (str): The time at which this event was generated in as an ISO-8601 string
    """

    detailType: constr(min_length=1)
    resources: List[constr(min_length=1)]
    account: constr(min_length=1)
    source: Literal["aws.braket"] = "aws.braket"
    time: int = int(datetime.utcnow().timestamp() * 1000)
