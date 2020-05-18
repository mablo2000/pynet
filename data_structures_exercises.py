#!/usr/bin/env python
"""
PyPlus Class 3 Exercises
"""
from pprint import pprint
import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

myfile = '../.netmiko.yml'
with open(myfile, 'r') as fin:
    device_list = yaml.load(fin)
cisco4 = device_list['cisco4']
net_connect = ConnectHandler(**cisco4)
show_run_output = net_connect.send_command("show run")

cisco_cfg = CiscoConfParse(show_run_output.splitlines())
interfaces_w_ip = cisco_cfg.find_objects_w_child(parentspec=r'^interface', childspec=r'^\s+ip address')
for interface in interfaces_w_ip:
    print('Interface Line:', interface.text)
    for childline in interface.children:
        print(childline)
