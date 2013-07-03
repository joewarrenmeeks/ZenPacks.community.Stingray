from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class StingrayEthernetInterface(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'StingrayEthernetInterface'

    _relations = ManagedEntity._relations + (
        ('nic', ToOne(ToManyCont,
            'ZenPacks.community.Stingray.StingrayDevice',
            'ethernet_interfaces',
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
        return self.nic()

    def getRRDTemplateName(self):
        return 'StingrayEthernetInterface'

