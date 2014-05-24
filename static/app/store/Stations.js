Ext.define('Pandora.store.Stations', {
    extend: 'Ext.data.Store',
		alias: 'store.test',
    requires: 'Pandora.model.Station',
    model: 'Pandora.model.Station',
	  proxy: {
			type: 'ajax',
			url: '/static/data/stations.json',
			reader: {
	     type: 'json',
       root: 'results'
	    }
			
		},
		autoLoad: true
});
