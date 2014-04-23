Ext.define("Sencha.view.ViewPort",{
	extend: "Ext.Panel",
	initialize: function(){},
	config:{
		fullscreen: true,
		layout: "card",
		items:[
			{xtype: "mainpanel"}
		]
	}
})
