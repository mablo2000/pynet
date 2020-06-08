from jinja2 import FileSystemLoader, Environment

nxos1 = {'interface': 'Ethernet1/1', 'ip_address': '10.1.100.1', 'netmask': '24'}
nxos2 = {'interface': 'Ethernet1/1', 'ip_address': '10.1.100.2', 'netmask': '24'}

env = Environment()
env.loader = FileSystemLoader("./templates/")
template = 'class5ex2a.j2'

for interface_info in (nxos1, nxos2):
    template = env.get_template(template)
    output = template.render(**interface_info)
    print(output)
