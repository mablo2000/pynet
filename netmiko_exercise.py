#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos"
}
nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}
cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios"
}
cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios"
}

net_connect= ConnectHandler(**cisco4)

cmd = "show version"
output = net_connect.send_command(cmd, use_textfsm=True)
print()
print(output)
print()

cmd = "show lldp neighbors"
output = net_connect.send_command(cmd, use_textfsm=True)
print()
print(output)
print()

net_connect.disconnect()
