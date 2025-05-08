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
    
    # print the raw XML in a "pretty" fashion
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    
    
    

   
    