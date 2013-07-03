from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo

from ZenPacks.community.Stingray.interfaces import (
    IStingrayDeviceInfo,
    IStingrayVirtualServerInfo,
    IStingrayPoolInfo,
    IStingrayNodeInfo,
    )

class StingrayVirtualServerInfo(ComponentInfo):
    implements(IStingrayVirtualServerInfo)

    virtualServerPort = ProxyProperty('virtualServerPort')
    virtualServerDefaultPool = ProxyProperty('virtualServerDefaultPool')

class StingrayPoolInfo(ComponentInfo):
    implements(IStingrayPoolInfo)

    poolAlgorithm = ProxyProperty('poolAlgorithm')

class StingrayNodeInfo(ComponentInfo):
    implements(IStingrayNodeInfo)

    nodePort = ProxyProperty('nodePort')
