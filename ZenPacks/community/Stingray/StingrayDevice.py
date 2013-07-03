from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class StingrayDevice(Device):


    # Define the relations.
    # Pools and VirtualServers can be treated as components.
    _relations = Device._relations + (
        ('pools', ToManyCont(ToOne,
            "ZenPacks.community.Stingray.StingrayPool", "pool")),
    ) + (
        ('virtual_servers', ToManyCont(ToOne, 
            "ZenPacks.community.Stingray.StingrayVirtualServer", 
            "virtual_server")),
    ) + (
        ('ethernet_interfaces', ToManyCont(ToOne,
            "ZenPacks.community.Stingray.StingrayEthernetInterface", "nic")),
    )



