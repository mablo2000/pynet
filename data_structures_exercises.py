#!/usr/bin/env python
"""
PyPlus Class 3 Exercises
"""
from pprint import pprint
import yaml

device_list = [
    {'device_name': 'cisco3', 'hostname': 'cisco3.lasthop.io', 'username': 'myname', 'password': 'mypass'},
    {'device_name': 'cisco4', 'hostname': 'cisco4.lasthop.io', 'username': 'myname', 'password': 'mypass'},
    {'device_name': 'arista1', 'hostname': 'arista1.lasthop.io', 'username': 'myname', 'password': 'mypass'},
    {'device_name': 'arista2', 'hostname': 'arista2.lasthop.io', 'username': 'myname', 'password': 'mypass'},
]

myfile = 'device_list.yaml'
with open('w', myfile) as fout:
    yaml.dump(device_list, myfile, default_flow_style=True, indent=4)

with open('r', myfile) as fin:
    device_list = yaml.load(fin)
pprint(device_list)
