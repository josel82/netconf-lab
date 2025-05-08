
from ncclient import manager, xml_
import xmltodict
import xml.dom.minidom
from gns3 import csr1000v



# Create an XML body to execute the save operation
body = """
<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
"""

# Connect to the Network Device
with manager.connect(
        host=csr1000v['address'],
        port=csr1000v['netconf_port'],
        username=csr1000v['username'],
        password=csr1000v['password'],
        hostkey_verify=False
    ) as m:

    print("Sending a RPC operation to the device.\n")
    # Use ncclient to send the RPC operation
    reply = m.dispatch(xml_.to_ele(body))

print("Raw XML reply from the device.\n")
# Print out the raw XML that returned
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())
print("")