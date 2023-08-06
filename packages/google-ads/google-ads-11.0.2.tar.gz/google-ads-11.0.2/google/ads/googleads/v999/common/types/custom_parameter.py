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

from google.ads.googleads.v999.common.types import mutate


__protobuf__ = proto.module(
    package="google.ads.googleads.v999.common",
    marshal="google.ads.googleads.v999",
    manifest={"CustomParameter", "CustomParameterOperation",},
)


class CustomParameter(proto.Message):
    r"""A mapping that can be used by custom parameter tags in a
    ``tracking_url_template``, ``final_urls``, or ``mobile_final_urls``.

    Attributes:
        key (str):
            The key matching the parameter tag name.
        value (str):
            The value to be substituted.
    """

    key = proto.Field(proto.STRING, number=3, optional=True,)
    value = proto.Field(proto.STRING, number=4, optional=True,)


class CustomParameterOperation(proto.Message):
    r"""Operation to be performed on a custom parameter list in a
    mutate.

    Attributes:
        operator (google.ads.googleads.v999.common.types.ListOperator.Enum):
            Type of list operation to perform.
        value (google.ads.googleads.v999.common.types.CustomParameter):
            The custom parameter being added or removed
            from the list. For the CLEAR operation, this
            should not be populated.
    """

    operator = proto.Field(proto.ENUM, number=1, enum=mutate.ListOperator.Enum,)
    value = proto.Field(proto.MESSAGE, number=2, message="CustomParameter",)


__all__ = tuple(sorted(__protobuf__.manifest))
