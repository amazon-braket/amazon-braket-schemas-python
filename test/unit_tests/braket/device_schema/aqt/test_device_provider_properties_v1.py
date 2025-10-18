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


import json
from braket.schema_common import BraketSchemaBase
from braket.device_schema.aqt.aqt_provider_properties_v1 import AqtProviderProperties


def test_schema_parse_obj():
    input = {
            "braketSchemaHeader": {
                "name": "braket.device_schema.aqt.aqt_provider_properties",
                "version": "1"
            },
            "properties": {
                    "readout_time_micros": 1500,
                    "mean_two_qubit_gate_fidelity": {
                        "uncertainty": 0.0019,
                        "value": 98.9
                    },
                    "single_qubit_gate_fidelity": {
                        "0": {
                            "uncertainty": 0.00002,
                            "value": 99.9998
                        },
                        "1": {
                            "uncertainty": 0.00003,
                            "value": 99.99972
                        },
                        "2": {
                            "uncertainty": 0.00007,
                            "value": 99.99941
                        },
                        "3": {
                            "uncertainty": 0.00004,
                            "value": 99.99969
                        },
                        "4": {
                            "uncertainty": 0.00003,
                            "value": 99.99973
                        },
                        "5": {
                            "uncertainty": 0.00002,
                            "value": 99.9998
                        },
                        "6": {
                            "uncertainty": 0.00004,
                            "value": 99.99952
                        },
                        "7": {
                            "uncertainty": 0.00007,
                            "value": 99.99956
                        },
                        "8": {
                            "uncertainty": 0.00003,
                            "value": 99.99962
                        },
                        "9": {
                            "uncertainty": 0.00002,
                            "value": 99.99979
                        },
                        "10": {
                            "uncertainty": 0.00008,
                            "value": 99.99932
                        },
                        "11": {
                            "uncertainty": 0.00002,
                            "value": 99.99978
                        }
                    },
                    "single_qubit_gate_duration_micros": 22,
                    "spam_fidelity_lower_bound": 99.74,
                    "t1_s": {
                        "uncertainty": 0.007,
                        "value": 1.168
                    },
                    "t2_coherence_time_s": {
                        "uncertainty": 31.3,
                        "value": 173.8
                    },
                    "two_qubit_gate_duration_micros": 660,
                    "updated_at": "2025-03-28T12:29:03"
            }
        }
    assert BraketSchemaBase.parse_raw_schema(json.dumps(input)) == AqtProviderProperties.parse_obj(input)
