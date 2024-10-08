# Copyright © 2019-2024 HQS Quantum Simulations GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
"""AQT backend for the qoqo quantum toolkit.

Allows the user to run qoqo Circuits on AQT simulators and AQT hardware (soon).
Note that a valid AQT access token is required to run circuits.

.. autosummary::
    :toctree: generated/

    Backend
    devices

"""

from .qoqo_aqt import *  # noqa: F403

__license__ = (
    "Apache-2.0 for linked dependencies see qoqo_aqt/LICENSE_FOR_BINARY_DISTRIBUTION"
)
