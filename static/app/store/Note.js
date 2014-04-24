Ext.define("Sencha.store.Note",{
	extend: "Ext.data.Store",
	requires: ["Sencha.model.Note"],
	config:{
		model: "Sencha.model.Note",
		proxy:{
			type: "ajax",
			url: '/news/info',
			reader:{
				type:"json",
				rootProperty:'news'
			}
		},
		autoLoad: true
	}
});
