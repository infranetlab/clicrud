#!/usr/bin/env python
"""
Copyright 2015 Brocade Communications Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from clicrud.device.generic import generic

transport = generic(host="172.27.181.121", username="admin", enable="password",
                    method="ssh", password="password")

# transport = generic(host="192.168.10.52", username="admin", enable="Passw0rd",
#                    method="ssh", password="Passw0rd")


print "===show version"
print transport.read("show version", return_type="string")

print "===configure stuff output"
print transport.configure(["interface TenGigabitEthernet 101/5/1",
                          "description TEST3"])

print "===show interface TenGigEth 101/5/1 | inc Description"
print transport.read("show interface ten 101/5/1 | inc Description", return_type="string")

transport.close()
