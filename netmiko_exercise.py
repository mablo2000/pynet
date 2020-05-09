#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

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
    "device_type": "cisco_nxos"
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
output = net_connect.send_command('ping', strip_prompt=False, strip_command=False, expect_string='Protocol')
output += net_connect.send_command('\n', strip_prompt=False, strip_command=False, expect_string='IP address')
output += net_connect.send_command('8.8.8.8', strip_prompt=False, strip_command=False, expect_string='Repeat')
output += net_connect.send_command('\n', strip_prompt=False, strip_command=False, expect_string='Datagram')
output += net_connect.send_command('\n', strip_prompt=False, strip_command=False, expect_string='Timeout')
output += net_connect.send_command('\n', strip_prompt=False, strip_command=False, expect_string='Extended')
output += net_connect.send_command('\n', strip_prompt=False, strip_command=False, expect_string='Sweep')
output += net_connect.send_command('\n', strip_prompt=False, strip_command=False)
net_connect.disconnect()

print()
print(output)
print()
