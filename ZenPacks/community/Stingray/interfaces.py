from Products.Zuul.form import schema
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.utils import ZuulMessageFactory as _t
from Products.Zuul.interfaces.component import IComponentInfo

class IStingrayDeviceInfo(IDeviceInfo):
    pass

class IStingrayVirtualServerInfo(IComponentInfo):
    virtualServerPort = schema.Int(title=_t('Port Number'))
    virtualServerDefaultPool = schema.TextLine(title=_t('Default Pool'))


class IStingrayPoolInfo(IComponentInfo):
    poolAlgorithm = schema.TextLine(title=_t('Algorithm'))

