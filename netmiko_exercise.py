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
    "global_delay_factor": 2
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

cmd = "show lldp neighbors detail"
net_connect= ConnectHandler(**nxos2)

start_time = datetime.now()
output = net_connect.send_command(cmd)
end_time = datetime.now()
print()
print(output)
print()
print("Execution Time: {}".format(end_time - start_time))
print()

start_time = datetime.now()
output = net_connect.send_command(cmd, delay_factor=8)
end_time = datetime.now()
print()
print(output)
print()
print("Execution Time: {}".format(end_time - start_time))
print()

net_connect.disconnect()
