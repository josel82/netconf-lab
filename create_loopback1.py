from ncclient import manager
from gns3 import csr1000v

# Create an XML configuration template for ietf-interfaces
netconf_interface_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>Loopback0</name>
            <description>Created with NETCONF</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                ianaift:softwareLoopback
            </type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>1.1.1.1</ip>
                    <netmask>255.255.255.255</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>"""

# Connect to the Network Device
with manager.connect(
    host=csr1000v['address'],
    port=csr1000v['netconf_port'],
    username=csr1000v['username'],
    password=csr1000v['password'],
    hostkey_verify=False
) as m:
# Send configuration
    csr1000v_createLoopback = m.edit_config(target = 'running', config = netconf_interface_template)
# Check status of the configuration 'True' means the configuration was applied successfully
    print(csr1000v_createLoopback.ok)