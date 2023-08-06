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
    manifest={"FinalUrlOperation",},
)


class FinalUrlOperation(proto.Message):
    r"""Operation to be performed on a final URL list in a mutate.
    Attributes:
        operator (google.ads.googleads.v999.common.types.ListOperator.Enum):
            Type of list operation to perform.
        value (str):
            The final URL being added or removed from the
            list. For the CLEAR operation, this should not
            be populated.
    """

    operator = proto.Field(proto.ENUM, number=1, enum=mutate.ListOperator.Enum,)
    value = proto.Field(proto.STRING, number=3, optional=True,)


__all__ = tuple(sorted(__protobuf__.manifest))
