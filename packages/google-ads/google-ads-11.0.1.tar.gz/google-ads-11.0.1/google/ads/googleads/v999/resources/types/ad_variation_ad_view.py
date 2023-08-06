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
    manifest={"AdVariationAdView",},
)


class AdVariationAdView(proto.Message):
    r"""An ad variation ad view that compares the performance between
    one pair of original ad and its variation ad created via Ad
    Variation Experiment. This resource is read only.

    Attributes:
        resource_name (str):
            Output only. The resource name of the ad variation ad view.
            Ad variation ad view resource names have the form:

            ``customers/{customer_id}/adVariationAdViews/{experiment_id}~{ad_group_id}~{base_ad_id}~{base_ad_version_id}~{experiment_ad_id}~{experiment_ad_version_id}``
    """

    resource_name = proto.Field(proto.STRING, number=1,)


__all__ = tuple(sorted(__protobuf__.manifest))
