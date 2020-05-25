import textfsm
from pprint import pprint


template_file = "ex2_show_int_status.tpl"
template = open(template_file)

with open("ex1_show_int_status.txt") as fin:
    status_input = fin.read()

re_table= textfsm.TextFSM(template)
data = re_table.ParseText(status_input)

template.close()

pprint(data)
