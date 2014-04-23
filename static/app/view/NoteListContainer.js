Ext.define("Sencha.view.NoteListContainer",{
	extend: "Ext.Panel",
	xtype: "notelistcontainer",
	requires:["Sencha.view.NoteList", "Sencha.view.SearchBar"],
	initialize: function(){
		var toolbar = {
			xtype: "toolbar",
			docked: "top",
			title: "Note List",
			items: [
				{
					xtype: "spacer"
				}, {
					xtype: "button",
					text: "Add",
					handler: this.onAddNoteTap,
					scope: this
				}
			]
		};
		this.add([toolbar,{xtype: "searchbar"}, {xtype: "notelist"}]);
	},
	config:{
		layout: "fit",
		title: "Note List",
		iconCls: "home"
	},
	onAddNoteTap: function(){
	}
});
