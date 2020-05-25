import textfsm
from pprint import pprint


template_file = "ex2_show_int_status.tpl"
template = open(template_file)

with open("ex1_show_int_status.txt") as fin:
    status_input = fin.read()

re_table= textfsm.TextFSM(template)
data = re_table.ParseText(status_input)

template.close()

show_int_status_list = []

for interface_info in data:
    port_name, status, vlan, duplex, speed, port_type = interface_info
    interface_dict = {'PORT_NAME': port_name,
                      'STATUS': status,
                      'VLAN': vlan,
                      'DUPLEX': duplex,
                      'SPEED': speed,
                      'PORT_TYPE': port_type}
    show_int_status_list.append(interface_dict)

pprint(data)
