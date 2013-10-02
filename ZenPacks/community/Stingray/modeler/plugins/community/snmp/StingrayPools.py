from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetMap, GetTableMap

from Products.DataCollector.plugins.DataMaps import MultiArgs, ObjectMap


class StingrayPools(SnmpPlugin):
    relname = "pools"
    modname = "ZenPacks.community.Stingray.StingrayPool"

    snmpGetTableMaps = (
        GetTableMap('poolTable', '.1.3.6.1.4.1.7146.1.2.3.2.1', {
            '.1': 'poolName',
            '.2': 'poolAlgorithm',
        }),
    )

    def process(self, device, results, log):
        log.info('processing %s for device %s', self.name(), device.id)

        # RelationshipMap for tables
        rm = self.relMap()
        pools = results[1].get('poolTable', {})

        for snmpindex, row in pools.items():
            name = row.get('poolName')

            if not name:
                log.warn('Skipping Pool with no name')
                continue

            if name == "discard":
                log.warn('Skipping discard pool')
                continue

            alg = self._zxtmalg(row.get('poolAlgorithm'))

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'poolAlgorithm': alg,
            }))

        return [rm]

    # Method to convert from number to ZXTM algorithm name

    def _zxtmalg(self, alg):

        try:
            algy = int(alg)
        except TypeError:
            print("{0} is not an integer".format(alg))

        if algy == 1:
            alg = "roundrobin"
        elif algy == 2:
            alg = "weightedRoundRobin"
        elif algy == 3:
            alg = "perceptive"
        elif algy == 4:
            alg = "leastConnections"
        elif algy == 5:
            alg = "fastestResponseTime"
        elif algy == 6:
            alg = "random"
        elif algy == 7:
            alg = "weightedLeastConnections"
        else:
            alg = "whiskytangofoxtrot"

        return alg
