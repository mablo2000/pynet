#!/usr/bin/env python
"""
PyPlus Class 3 Exercises
"""
from pprint import pprint
import yaml

myfile = '~/.netmiko.yml'
with open(myfile, 'r') as fin:
    device_list = yaml.load(fin)
pprint(device_list)
