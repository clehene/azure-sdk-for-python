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


class FirewallRuleProperties(Model):
    """Data Lake Store firewall rule properties information.

    :param start_ip_address: the start IP address for the firewall rule.
    :type start_ip_address: str
    :param end_ip_address: the end IP address for the firewall rule.
    :type end_ip_address: str
    """ 

    _attribute_map = {
        'start_ip_address': {'key': 'startIpAddress', 'type': 'str'},
        'end_ip_address': {'key': 'endIpAddress', 'type': 'str'},
    }

    def __init__(self, start_ip_address=None, end_ip_address=None):
        self.start_ip_address = start_ip_address
        self.end_ip_address = end_ip_address
