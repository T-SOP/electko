Ext.Loader.setPath({
	'Ext': 'lib/src',
	'Pandora': '/static/app'
})

Ext.application({
    name: 'Pandora',
    
    autoCreateViewport: true,
    
    models: ['Station'],    
    stores: ['Stations'],
    controllers: ['Station']
});
