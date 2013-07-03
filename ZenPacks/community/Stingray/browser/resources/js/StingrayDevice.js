(function() {

var ZC = Ext.ns('Zenoss.component');




ZC.StingrayVirtualServerPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'StingrayVirtualServer',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'virtualServerPort'},
                {name: 'virtualServerDefaultPool'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true,
                width: 150
            },{
                id: 'virtualServerPort',
                dataIndex: 'virtualServerPort',
                header: _t('Port'),
                sortable: true,
                width: 50
            },{
                id: 'virtualServerDefaultPool',
                dataIndex: 'virtualServerDefaultPool',
                header: _t('Default Pool'),
                sortable: true,
                width: 100
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });
        ZC.StingrayVirtualServerPanel.superclass.constructor.call( this, config);
    }
});

Ext.reg('StingrayVirtualServerPanel', ZC.StingrayVirtualServerPanel);

ZC.registerName(
  'StingrayVirtualServer',
  _t('Virtual Server'),
  _t('Virtual Servers'));


ZC.StingrayPoolPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'StingrayPool',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'poolAlgorithm'},
                {name: 'locking'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true,
                width: 150
            },{
                id: 'poolAlgorithm',
                dataIndex: 'poolAlgorithm',
                header: _t('Default Alg'),
                sortable: true,
                width: 100
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });
        ZC.StingrayPoolPanel.superclass.constructor.call( this, config);
  }
});

Ext.reg('StingrayPoolPanel', ZC.StingrayPoolPanel);

ZC.registerName(
  'StingrayPool',
  _t('Stingray Pool'),
  _t('Stingray Pools'));

ZC.registerName(
    'StingrayEthernetInterface',
    _t('Ethernet Interface'),
    _t('Ethernet Interfaces'));

})();

