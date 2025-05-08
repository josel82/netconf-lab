from ncclient import manager
from gns3 import csr1000v

with manager.connect(
    host=csr1000v['address'],
    port=csr1000v['netconf_port'],
    username=csr1000v['username'],
    password=csr1000v['password'],
    hostkey_verify=False
) as m:
    for capability in m.server_capabilities:
        print(capability)

     



