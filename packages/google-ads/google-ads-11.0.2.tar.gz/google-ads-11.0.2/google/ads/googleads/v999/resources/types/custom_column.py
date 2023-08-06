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

from google.ads.googleads.v999.enums.types import custom_column_value_type


__protobuf__ = proto.module(
    package="google.ads.googleads.v999.resources",
    marshal="google.ads.googleads.v999",
    manifest={"CustomColumn",},
)


class CustomColumn(proto.Message):
    r"""A custom column.
    See Google Ads custom column at
    https://support.google.com/google-ads/answer/3073556

    Attributes:
        resource_name (str):
            Immutable. The resource name of the custom column. Custom
            column resource names have the form:

            ``customers/{customer_id}/customColumns/{custom_column_id}``
        id (int):
            Output only. ID of the custom column.
        name (str):
            Output only. User-defined name of the custom
            column.
        description (str):
            Output only. User-defined description of the
            custom column.
        value_type (google.ads.googleads.v999.enums.types.CustomColumnValueTypeEnum.CustomColumnValueType):
            Output only. The type of the result value of
            the custom column.
        references_attributes (bool):
            Output only. True when the custom column is
            referring to one or more attributes.
        references_metrics (bool):
            Output only. True when the custom column is
            referring to one or more metrics.
        queryable (bool):
            Output only. True when the custom column is
            available to be used in the query of
            GoogleAdsService.Search and
            GoogleAdsService.SearchStream.
        referenced_system_columns (Sequence[str]):
            Output only. The list of the referenced
            system columns of this custom column. E.g. A
            custom column "sum of impressions and clicks"
            has referenced system columns of
            {"metrics.clicks", "metrics.impressions"}.
    """

    resource_name = proto.Field(proto.STRING, number=1,)
    id = proto.Field(proto.INT64, number=2,)
    name = proto.Field(proto.STRING, number=3,)
    description = proto.Field(proto.STRING, number=4,)
    value_type = proto.Field(
        proto.ENUM,
        number=5,
        enum=custom_column_value_type.CustomColumnValueTypeEnum.CustomColumnValueType,
    )
    references_attributes = proto.Field(proto.BOOL, number=6,)
    references_metrics = proto.Field(proto.BOOL, number=7,)
    queryable = proto.Field(proto.BOOL, number=8,)
    referenced_system_columns = proto.RepeatedField(proto.STRING, number=9,)


__all__ = tuple(sorted(__protobuf__.manifest))
