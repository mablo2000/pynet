#!/usr/bin/env python
"""
PyPlus Class 3 Exercises
"""
from pprint import pprint

device_list = [
    {'device_name': 'cisco3', 'hostname': 'cisco3.lasthop.io', 'username': 'myname', 'password': 'mypass'},
    {'device_name': 'cisco4', 'hostname': 'cisco4.lasthop.io', 'username': 'myname', 'password': 'mypass'},
    {'device_name': 'arista1', 'hostname': 'arista1.lasthop.io', 'username': 'myname', 'password': 'mypass'},
    {'device_name': 'arista2', 'hostname': 'arista2.lasthop.io', 'username': 'myname', 'password': 'mypass'},
]

pprint(device_list)
