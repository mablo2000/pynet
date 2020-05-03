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

device_list = (nxos1, nxos2)
for device in device_list:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.disconnect()

net_connect= ConnectHandler(**cisco3)
output = net_connect.send_command('show version')

fout = open('show_version.txt', 'w')
fout.write(output)
net_connect.disconnect()
