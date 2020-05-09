#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
import time

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
    "device_type": "cisco_ios",
    "fast_cli": True
}
cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt"
}

net_connect= ConnectHandler(**cisco4)

output = net_connect.find_prompt()
print(output)
net_connect.config_mode()
output = net_connect.find_prompt()
print(output)
net_connect.exit_config_mode()
output = net_connect.find_prompt()
print(output)
net_connect.write_channel('disable\n')
time.sleep(2)
output = net_connect.read_channel()
print(output)
net_connect.enable()
output = net_connect.find_prompt()
print(output)
net_connect.disconnect()
