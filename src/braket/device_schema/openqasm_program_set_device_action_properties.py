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

from pydantic.v1 import conint, constr

from braket.device_schema.device_action_properties import DeviceActionProperties


class OpenQASMProgramSetDeviceActionProperties(DeviceActionProperties):
    """
    Defines the properties for the Braket OpenQASM program set action.

    Attributes:
        maximumExecutables(int): The maximum number of executables
            that can be in a single program set.
        maximumTotalShots(int): The maximum allowed total shots across all
            executables in a single program set.
        minimumTotalShots(int | None): The minimum allowed total shots
            across all executables in a single program set. When unset, no
            task-level minimum is enforced. Devices opt in by setting this
            field to a value > 1.
    """

    actionType: constr(regex=r"^braket\.ir\.openqasm\.program_set$")
    maximumExecutables: conint(ge=0)
    maximumTotalShots: conint(ge=0)
    minimumTotalShots: conint(ge=1) | None = None
