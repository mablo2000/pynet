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

myfile = 'arista_arp.json'
arp_entries = dict()
with open(myfile, 'r') as fin:
    arp_output = json.load(fin)
v4_neighbors_list = arp_output['ipV4Neighbors']
for arp_entry in v4_neighbors_list:
    arp_entries[arp_entry['address']] = arp_entry['hwAddress']
pprint(arp_entries)
