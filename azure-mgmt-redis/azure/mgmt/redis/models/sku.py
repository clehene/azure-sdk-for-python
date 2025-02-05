# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Sku(Model):
    """Sku parameters supplied to the create redis operation.

    :param name: What type of redis cache to deploy. Valid values: (Basic,
     Standard, Premium). Possible values include: 'Basic', 'Standard',
     'Premium'
    :type name: str or :class:`SkuName <azure.mgmt.redis.models.SkuName>`
    :param family: Which family to use. Valid values: (C, P). Possible values
     include: 'C', 'P'
    :type family: str or :class:`SkuFamily
     <azure.mgmt.redis.models.SkuFamily>`
    :param capacity: What size of redis cache to deploy. Valid values: for C
     family (0, 1, 2, 3, 4, 5, 6), for P family (1, 2, 3, 4)
    :type capacity: int
    """ 

    _validation = {
        'name': {'required': True},
        'family': {'required': True},
        'capacity': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, name, family, capacity):
        self.name = name
        self.family = family
        self.capacity = capacity
