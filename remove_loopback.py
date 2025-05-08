from ncclient import manager
from gns3 import csr1000v, IETF_INTERFACE_TYPES



template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
            <name>{name}</name>
        </interface>
    </interfaces>
</config>"""



data = template.format(
        name="Loopback"+input("Loopback number: ")
    )

with manager.connect(
    host=csr1000v['address'],
    port=csr1000v['netconf_port'],
    username=csr1000v['username'],
    password=csr1000v['password'],
    hostkey_verify=False
) as m:

# Send configuration
    createLoopback = m.edit_config(data, target = 'running')
# Check status of the configuration 'True' means the configuration was applied successfully
    print(createLoopback.ok)