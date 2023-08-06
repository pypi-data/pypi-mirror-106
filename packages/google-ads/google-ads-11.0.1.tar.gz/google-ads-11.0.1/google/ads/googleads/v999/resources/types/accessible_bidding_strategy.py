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

from google.ads.googleads.v999.enums.types import bidding_strategy_type


__protobuf__ = proto.module(
    package="google.ads.googleads.v999.resources",
    marshal="google.ads.googleads.v999",
    manifest={"AccessibleBiddingStrategy",},
)


class AccessibleBiddingStrategy(proto.Message):
    r"""Represents a view of BiddingStrategies owned by and shared
    with the customer.
    In contrast to BiddingStrategy, this resource includes
    strategies owned by managers of the customer and shared with
    this customer - in addition to strategies owned by this
    customer. This resource does not provide metrics and only
    exposes a limited subset of the BiddingStrategy attributes.

    Attributes:
        resource_name (str):
            Output only. The resource name of the accessible bidding
            strategy. AccessibleBiddingStrategy resource names have the
            form:

            ``customers/{customer_id}/accessibleBiddingStrategies/{bidding_strategy_id}``
        id (int):
            Output only. The ID of the bidding strategy.
        name (str):
            Output only. The name of the bidding
            strategy.
        type_ (google.ads.googleads.v999.enums.types.BiddingStrategyTypeEnum.BiddingStrategyType):
            Output only. The type of the bidding
            strategy.
        owner_customer_id (int):
            Output only. The ID of the Customer which
            owns the bidding strategy.
        owner_descriptive_name (str):
            Output only. descriptive_name of the Customer which owns the
            bidding strategy.
    """

    resource_name = proto.Field(proto.STRING, number=1,)
    id = proto.Field(proto.INT64, number=2,)
    name = proto.Field(proto.STRING, number=3,)
    type_ = proto.Field(
        proto.ENUM,
        number=4,
        enum=bidding_strategy_type.BiddingStrategyTypeEnum.BiddingStrategyType,
    )
    owner_customer_id = proto.Field(proto.INT64, number=5,)
    owner_descriptive_name = proto.Field(proto.STRING, number=6,)


__all__ = tuple(sorted(__protobuf__.manifest))
