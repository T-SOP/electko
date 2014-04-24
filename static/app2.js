Ext.Loader.setPath({
	'Ext': 'lib/src',
	'Sencha': '/static/app'
})


Ext.application({
	name: 'Sencha',
//define the startupscreens for tablet and phone, as well as the icon
icon: {
	57: 'resources/icons/icon.png',
72: 'resources/icons/icon@72.png',
114: 'resources/icons/icon@2x.png',
144: 'resources/icons/icon@144.png'
},
phoneIcon: "resources/icons/images/app-phone-icon.png",
	
	models:["Note"],
	stores:["Note"],
	views: ["ViewPort","MainPanel", "NoteListContainer"],
	launch: function() {
			Ext.create('Sencha.view.ViewPort')
		}
});

