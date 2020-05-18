#!/usr/bin/env python
"""
PyPlus Class 3 Exercises
"""
from pprint import pprint
import yaml
from netmiko import ConnectHandler


myfile = '../.netmiko.yml'
with open(myfile, 'r') as fin:
    device_list = yaml.load(fin)
cisco3 = device_list['cisco3']
net_connect = ConnectHandler(**cisco3)
output = net_connect.find_prompt()
pprint(output)
