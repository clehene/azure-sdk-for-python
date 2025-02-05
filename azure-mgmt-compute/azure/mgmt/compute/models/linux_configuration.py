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


class LinuxConfiguration(Model):
    """
    Describes Windows Configuration of the OS Profile.

    :param disable_password_authentication: Gets or sets whether
     Authentication using user name and password is allowed or not
    :type disable_password_authentication: bool
    :param ssh: Gets or sets the SSH configuration for linux VMs
    :type ssh: :class:`SshConfiguration
     <azure.mgmt.compute.models.SshConfiguration>`
    """ 

    _attribute_map = {
        'disable_password_authentication': {'key': 'disablePasswordAuthentication', 'type': 'bool'},
        'ssh': {'key': 'ssh', 'type': 'SshConfiguration'},
    }

    def __init__(self, disable_password_authentication=None, ssh=None):
        self.disable_password_authentication = disable_password_authentication
        self.ssh = ssh
