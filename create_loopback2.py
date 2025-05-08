from ncclient import manager
from gns3 import csr1000v, IETF_INTERFACE_TYPES





# XML configuration template for ietf-interfaces
int_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{name}</name>
            <description>{desc}</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                {type}
            </type>
            <enabled>{status}</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>{ip_address}</ip>
                    <netmask>{mask}</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>"""

loopback = {}
loopback["name"] = "Loopback" + input("Loopback number: ")
loopback["desc"] = input("Add a description: ")
loopback["type"] = IETF_INTERFACE_TYPES["loopback"]
loopback["status"] = "true"
loopback["ip_address"] = input("IP address: ")
loopback["mask"] = input("Network mask: ")


data = int_template.format(
        name = loopback["name"],
        desc = loopback["desc"],
        type = loopback["type"],
        status = loopback["status"],
        ip_address = loopback["ip_address"],
        mask = loopback["mask"]
    )

# Connect to the Network Device
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