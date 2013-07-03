from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class StingrayPool(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'StingrayPool'

    # Need these for the javascripty column headers
    poolName = ""
    poolAlgorithm = ""
    snmpindex = -1

    _properties = ManagedEntity._properties + (
        {'id': 'poolName', 'type': 'string'},
        {'id': 'poolAlgorithm', 'type': 'string'},
    )

    _relations = ManagedEntity._relations + (
        ('pool', ToOne(ToManyCont, 
		'ZenPacks.community.Stingray.StingrayDevice', 'pools')),
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
        return self.pool()

    def getRRDTemplateName(self):
        return 'StingrayPool' 

