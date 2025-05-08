from ncclient import manager
from gns3 import csr1000v
import xmltodict
import xml.dom.minidom


netconf_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface></interface>
    </interfaces>
</filter>"""

with manager.connect(
    host=csr1000v['address'],
    port=csr1000v['netconf_port'],
    username=csr1000v['username'],
    password=csr1000v['password'],
    hostkey_verify=False
) as m:

    netconf_reply = m.get_config(source = 'running', filter = netconf_filter)

    # Parse the returned XML to an Ordered Dictionary
    netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

    # Getting the name of the interface
    interfaces = netconf_data["interfaces"]["interface"]
    
    for interface in interfaces:
        print("Interface {} enabled status is {}".format(
            interface["name"],
            interface["enabled"]
            )
        )
    
    
    

   
    