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

net_connect= ConnectHandler(**cisco3)

cmd = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]
start_time = datetime.now()
output = net_connect.send_config_set(cmd)
end_time = datetime.now()
print()
print(output)
print()
print('Execution Time: {}'.format(end_time - start_time))
print()

cmd = "ping google.com"
output = net_connect.send_command(cmd)
print()
print(output)
print()

net_connect.disconnect()
