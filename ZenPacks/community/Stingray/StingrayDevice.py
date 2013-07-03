from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class StingrayDevice(Device):

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
    ) + (
        ('nodes', ToManyCont(ToOne,
            "ZenPacks.community.Stingray.StingrayNode", "node")),
    )


