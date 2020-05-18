#!/usr/bin/env python
"""
PyPlus Class 3 Exercises
"""
from pprint import pprint
import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

bgp_config_snippet = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""
peer_list = []
cisco_cfg = CiscoConfParse(bgp_config_snippet.splitlines())
neighbors = cisco_cfg.find_objects_w_child(parentspec=r'^\s+neighbor', childspec=r'remote-as')
for neighbor in neighbors:
    neighbor_ip = neighbor.text.split()[1]
    remote_as = neighbor.re_search_children(r'remote-as')[0].split()[1]
    peer_list.append((neighbor_ip, remote_as))
pprint(peer_list)
