from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetMap, GetTableMap

from Products.DataCollector.plugins.DataMaps import MultiArgs, ObjectMap


class StingrayEthernetInterfaces(SnmpPlugin):
    relname = "ethernet_interfaces"
    modname = "ZenPacks.community.Stingray.StingrayEthernetInterface"

    snmpGetTableMaps = (
        GetTableMap('interfaceTable', '.1.3.6.1.4.1.7146.1.2.12.2.1', {
        '.1': 'interfaceName',
        }),
    )

    def process(self, device, results, log):
        log.info('processing %s for device %s', self.name(), device.id)

        # RelationshipMap for tables
        rm = self.relMap()
        interfaces = results[1].get('interfaceTable', {})

        for snmpindex, row in interfaces.items():
            name = row.get('interfaceName')

            if not name:
                log.warn('Skipping interface with no name')
                continue

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
            }))

        return [rm]

