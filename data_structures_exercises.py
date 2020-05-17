#!/usr/bin/env python
"""
PyPlus Class 3 Exercises
"""
from pprint import pprint

show_arp_data = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

arp_entries = []

for line in show_arp_data.splitlines():
    if 'Protocol' not in line and line != '\n':
        print(line)
        protocol, ip_address, age, mac_address, type, interface = line.split()
        entry_dict = {"mac_addr": mac_address, "ip_addr": ip_address, "interface": interface}
        arp_entries.append(entry_dict)
pprint(arp_entries)
