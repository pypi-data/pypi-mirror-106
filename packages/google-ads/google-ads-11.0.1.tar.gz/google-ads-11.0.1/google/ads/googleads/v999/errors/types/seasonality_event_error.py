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
    package="google.ads.googleads.v999.errors",
    marshal="google.ads.googleads.v999",
    manifest={"SeasonalityEventErrorEnum",},
)


class SeasonalityEventErrorEnum(proto.Message):
    r"""Container for enum describing possible seasonality event
    errors.
        """

    class SeasonalityEventError(proto.Enum):
        r"""Enum describing possible seasonality event errors."""
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_START_TIME = 2
        INVALID_END_TIME = 3
        INVALID_TIME_RANGE = 4
        UNSUPPORTED_DEVICE_TYPE = 5
        ADVERTISING_CHANNEL_TYPES_NOT_ALLOWED = 6
        ADVERTISING_CHANNEL_TYPES_REQUIRED = 7
        UNSUPPORTED_ADVERTISING_CHANNEL_TYPE = 8
        CAMPAIGN_IDS_NOT_ALLOWED = 9
        CAMPAIGN_IDS_REQUIRED = 10
        CANNOT_MODIFY_REMOVED_EVENT = 11
        SCOPE_NOT_ALLOWED = 12


__all__ = tuple(sorted(__protobuf__.manifest))
