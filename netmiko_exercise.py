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
    "device_type": "cisco_ios",
    "fast_cli": True
}
cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios"
}

config_file = 'nxos_vlans.cfg'
nxos = [nxos1,nxos2]
for router in nxos:
    net_connect= ConnectHandler(**router)

    output = net_connect.send_config_from_file(config_file)
    output += net_connect.save_config()
    print()
    print(output)
    print()

    net_connect.disconnect()
