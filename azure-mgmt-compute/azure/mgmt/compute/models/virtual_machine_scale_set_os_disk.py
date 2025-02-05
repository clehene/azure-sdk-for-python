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


class VirtualMachineScaleSetOSDisk(Model):
    """
    Describes a virtual machine scale set operating system disk.

    :param name: Gets or sets the disk name.
    :type name: str
    :param caching: Gets or sets the caching type. Possible values include:
     'None', 'ReadOnly', 'ReadWrite'
    :type caching: str or :class:`CachingTypes
     <azure.mgmt.compute.models.CachingTypes>`
    :param create_option: Gets or sets the create option. Possible values
     include: 'fromImage', 'empty', 'attach'
    :type create_option: str or :class:`DiskCreateOptionTypes
     <azure.mgmt.compute.models.DiskCreateOptionTypes>`
    :param os_type: Gets or sets the Operating System type. Possible values
     include: 'Windows', 'Linux'
    :type os_type: str or :class:`OperatingSystemTypes
     <azure.mgmt.compute.models.OperatingSystemTypes>`
    :param image: Gets or sets the Source User Image VirtualHardDisk. This
     VirtualHardDisk will be copied before using it to attach to the Virtual
     Machine.If SourceImage is provided, the destination VirtualHardDisk
     should not exist.
    :type image: :class:`VirtualHardDisk
     <azure.mgmt.compute.models.VirtualHardDisk>`
    :param vhd_containers: Gets or sets the list of virtual hard disk
     container uris.
    :type vhd_containers: list of str
    """ 

    _validation = {
        'name': {'required': True},
        'create_option': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'caching': {'key': 'caching', 'type': 'CachingTypes'},
        'create_option': {'key': 'createOption', 'type': 'DiskCreateOptionTypes'},
        'os_type': {'key': 'osType', 'type': 'OperatingSystemTypes'},
        'image': {'key': 'image', 'type': 'VirtualHardDisk'},
        'vhd_containers': {'key': 'vhdContainers', 'type': '[str]'},
    }

    def __init__(self, name, create_option, caching=None, os_type=None, image=None, vhd_containers=None):
        self.name = name
        self.caching = caching
        self.create_option = create_option
        self.os_type = os_type
        self.image = image
        self.vhd_containers = vhd_containers
