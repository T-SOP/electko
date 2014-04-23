Ext.define('Sencha.store.News',{
	alias: 'store.News',
	extend: 'Ext.data.Store',
	requires: ['Sencha.model.News'],
	config:{
		model: 'Sencha.model.News',
		sorters: 'author',
		autoLoad: true,
		grouper:{
			groupFn: function(record){
				return record.get('author');
			}
		},
		proxy:{
			type:'ajax',
			url: '/news/info',
			render:{
				type:'json',
				rootProperty:'news'
			}
		}
	}
});
