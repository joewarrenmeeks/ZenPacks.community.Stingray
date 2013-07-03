from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetMap, GetTableMap

from Products.DataCollector.plugins.DataMaps import MultiArgs, ObjectMap


class StingrayVirtualServers(SnmpPlugin):
    relname = "virtual_servers"
    modname = "ZenPacks.community.Stingray.StingrayVirtualServer"

    snmpGetTableMaps = (
        GetTableMap('virtualServerTable', '.1.3.6.1.4.1.7146.1.2.2.2.1', {
            '.1': 'virtualServerName',
            '.2': 'virtualServerPort',
            '.4': 'virtualServerDefaultPool',
        }),
    )

    def process(self, device, results, log):
        log.info('processing %s for device %s', self.name(), device.id)

        # RelationshipMap for tables
        rm = self.relMap()
        virtualservers = results[1].get('virtualServerTable', {})

        for snmpindex, row in virtualservers.items():
            name = row.get('virtualServerName')

            if not name:
                log.warn('Skipping Virtual Server with no name')
                continue

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'virtualServerDefaultPool': row.get('virtualServerDefaultPool'),
                'virtualServerPort': row.get('virtualServerPort'),
            }))

        return [rm]

