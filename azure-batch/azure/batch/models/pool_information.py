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


class PoolInformation(Model):
    """Specifies how a job should be assigned to a pool.

    :param pool_id: The id of an existing pool. All the tasks of the job will
     run on the specified pool. You must specify either PoolId or
     AutoPoolSpecification, but not both.
    :type pool_id: str
    :param auto_pool_specification: Characteristics for a temporary 'auto
     pool'. The Batch service will create this auto pool and run all of the
     tasks of the job on it, and will delete the pool once the job has
     completed. You must specify either PoolId or AutoPoolSpecification, but
     not both.
    :type auto_pool_specification: :class:`AutoPoolSpecification
     <azure.batch.models.AutoPoolSpecification>`
    """ 

    _attribute_map = {
        'pool_id': {'key': 'poolId', 'type': 'str'},
        'auto_pool_specification': {'key': 'autoPoolSpecification', 'type': 'AutoPoolSpecification'},
    }

    def __init__(self, pool_id=None, auto_pool_specification=None):
        self.pool_id = pool_id
        self.auto_pool_specification = auto_pool_specification
