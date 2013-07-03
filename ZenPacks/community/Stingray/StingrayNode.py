from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class StingrayNode(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'StingrayNode'

    nodeName = ""
    nodePort = -1
    snmpindex = -1

    _properties = ManagedEntity._properties + (
        {'id': 'nodeName', 'type': 'string'},
        {'id': 'nodePort', 'type': 'int'},
    )

    _relations = ManagedEntity._relations + (
        ('node', ToOne(ToManyCont, 
		'ZenPacks.community.Stingray.StingrayDevice', 'nodes')),
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
        return self.node()

    def getRRDTemplateName(self):
        return 'StingrayNode' 

