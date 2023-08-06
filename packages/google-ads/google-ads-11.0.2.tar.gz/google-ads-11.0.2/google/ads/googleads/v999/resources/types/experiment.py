# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v999.resources",
    marshal="google.ads.googleads.v999",
    manifest={"Experiment",},
)


class Experiment(proto.Message):
    r"""A Google ads experiment for users to experiment changes on
    multiple campaigns, compare the performance, and apply the
    effective changes.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the experiment. Experiment
            resource names have the form:

            ``customers/{customer_id}/experiments/{experiment_id}``
        experiment_id (int):
            Output only. The ID of the experiment. Read
            only.
    """

    resource_name = proto.Field(proto.STRING, number=1,)
    experiment_id = proto.Field(proto.INT64, number=9, optional=True,)


__all__ = tuple(sorted(__protobuf__.manifest))
