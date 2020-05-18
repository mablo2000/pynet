#!/usr/bin/env python
"""
PyPlus Class 3 Exercises
"""
from pprint import pprint
import json

device_list = [
    {'device_name': 'cisco3', 'hostname': 'cisco3.lasthop.io', 'username': 'myname', 'password': 'mypass'},
    {'device_name': 'cisco4', 'hostname': 'cisco4.lasthop.io', 'username': 'myname', 'password': 'mypass'},
    {'device_name': 'arista1', 'hostname': 'arista1.lasthop.io', 'username': 'myname', 'password': 'mypass'},
    {'device_name': 'arista2', 'hostname': 'arista2.lasthop.io', 'username': 'myname', 'password': 'mypass'},
]

myfile = 'napalm_unit_test.json'
ipv4_list = []
ipv6_list = []
with open(myfile, 'r') as fin:
    napalm_unit_test = json.load(fin)
for interface, interface_dict in napalm_unit_test.items():
    for protocol in interface_dict.keys():
        if protocol == 'ipv4':
            for ip_address, address_dict in interface_dict[protocol].items():
                prefix_length = address_dict['prefix_length']
                ipv4_list.append(ip_address + '/' + prefix_length)
        elif protocol == 'ipv6':
            for ip_address, address_dict in interface_dict[protocol].items():
                prefix_length = address_dict['prefix_length']
                ipv6_list.append(ip_address + '/' + prefix_length)
