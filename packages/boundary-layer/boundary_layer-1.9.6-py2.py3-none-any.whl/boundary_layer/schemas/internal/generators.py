# -*- coding: utf-8 -*-
# Copyright 2018 Etsy Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

import marshmallow as ma
from boundary_layer.schemas.internal.base import BaseSpecSchema


class GeneratorSpecSchema(BaseSpecSchema):
    iterator_builder_method_code = ma.fields.String(required=True)
    item_name_builder_code = ma.fields.String(required=True)
