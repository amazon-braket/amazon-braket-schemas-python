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

import fileinput
from pathlib import Path

# Here we replace the `amazon-braket-schemas` dependency to point to the file
# system; otherwise pip will install them separately, allowing it to override the version of
# any mutual dependencies with the schemas. By pointing to the file system, pip will be
# forced to reconcile the dependencies with the dependencies of the schemas,
# and raise an error if there are conflicts.

package = "amazon-braket-schemas"
path = Path.cwd().parent.resolve()

# Determine which config file exists
if Path("setup.py").exists():
    config_file = "setup.py"
elif Path("pyproject.toml").exists():
    config_file = "pyproject.toml"
else:
    raise FileNotFoundError("Neither setup.py nor pyproject.toml found")

for line in fileinput.input(config_file, inplace=True):
    replaced_line = (
        line if package not in line else f'    "{package} @ file://{path}/{package}-python",\n'
    )
    print(replaced_line, end="")
