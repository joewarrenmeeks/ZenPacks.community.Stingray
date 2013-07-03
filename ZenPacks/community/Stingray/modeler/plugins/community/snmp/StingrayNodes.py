from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetMap, GetTableMap

from Products.DataCollector.plugins.DataMaps import MultiArgs, ObjectMap


class StingrayNodes(SnmpPlugin):
    relname = "nodes"
    modname = "ZenPacks.community.Stingray.StingrayNode"

    snmpGetTableMaps = (
        GetTableMap('nodeTable', '.1.3.6.1.4.1.7146.1.2.4.4.1', {
            '.3.1': 'nodePort',
            '.4.1': 'nodeName',
        }),
    )

    def process(self, device, results, log):
        log.info('processing %s for device %s', self.name(), device.id)

        # RelationshipMap for tables
        rm = self.relMap()
        pools = results[1].get('nodeTable', {})

        for snmpindex, row in pools.items():
            name = row.get('nodeName')

            if not name:
                log.warn('Skipping Node with no name')
                continue

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'nodePort': row.get('nodePort'),
            }))

        return [rm]

