from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class StingrayVirtualServer(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'StingrayVirtualServer'

    # Again, these are used for the column headers
    virtualServerName = ""
    virtualServerDefaultPool = ""
    snmpindex = -1
    virtualServerPort = 0

    _properties = ManagedEntity._properties + (
        {'id': 'virtualServerName', 'type': 'string'},
        {'id': 'virtualServerDefaultPool', 'type': 'string'},
        {'id': 'virtualServerPort', 'type': 'int'},
    )

    _relations = ManagedEntity._relations + (
        ('virtual_server', ToOne(ToManyCont,
            'ZenPacks.community.Stingray.StingrayDevice',
            'virtual_servers',
            )),
    )


    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
            },),
        },)

    def device(self):
        return self.virtual_server()

    def getRRDTemplateName(self):
        return 'StingrayVirtualServer'


