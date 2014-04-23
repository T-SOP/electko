Ext.Loader.setPath({
	'Ext': 'lib/src',
})


Ext.application({
	name: 'Sencha',

//define the startupscreens for tablet and phone, as well as the icon
startupImage: {
	'320x460': 'resources/startup/Default.jpg', // Non-retina iPhone, iPod touch, and all Android devices
'640x920': 'resources/startup/640x920.png', // Retina iPhone and iPod touch
'640x1096': 'resources/startup/640x1096.png', // iPhone 5 and iPod touch (fifth generation)
'768x1004': 'resources/startup/768x1004.png', //  Non-retina iPad (first and second generation) in portrait orientation
'748x1024': 'resources/startup/748x1024.png', //  Non-retina iPad (first and second generation) in landscape orientation
'1536x2008': 'resources/startup/1536x2008.png', // : Retina iPad (third generation) in portrait orientation
'1496x2048': 'resources/startup/1496x2048.png' // : Retina iPad (third generation) in landscape orientation
},

isIconPrecomposed: false,
icon: {
	57: 'resources/icons/icon.png',
72: 'resources/icons/icon@72.png',
114: 'resources/icons/icon@2x.png',
144: 'resources/icons/icon@144.png'
},
	launch: function() {
		console.log('this launch run');
		var listConfiguration = this.getListConfiguration();
		if(!Ext.os.is.Phone){
			Ext.Viewport.add({
				xtype: 'panel',
				width: "100%",
				height: "100%",
				centered: true,
				modal: true,
				hideOnMaskTap: false,
				layout: 'fit',
				items: [listConfiguration]
			})
		}else{
			Ext.Viewport.add(listConfiguration);
		}
	},
	getListConfiguration: function() {
		var store = Ext.create('Ext.data.Store',{
			fields: ['title','link','description','author','content'],
			sorters: 'author',
			autoLoad: true,
			grouper: {
				groupFn: function(record){
					return record.get('author');
				}
			},
			proxy:{
				type:'ajax',
				url:'/news/info',
				reader:{
					type:'json',
					rootProperty: "news"
				}
			}
		});
		return {
			xtype: 'list',
			id: 'list',
			itemTpl: '{title} [{author}] <br /> {link}<br/>{description}',
			grouped:true,
			indexBar: true,
			infinite: true,
			useSimpleItems: true,
			variableHeights: true,
			striped: true,
			ui: 'round',
			store: store
		};
	}
});

