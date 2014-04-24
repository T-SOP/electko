Ext.define("Sencha.model.Note",{
	extend: "Ext.data.Model",
	config:{
		idProperty: "link",
		fields:[
			{name: "link", type: "string"},
			{name: "title", type: "string"},
			{name: "author", type: "string"},
			{name: "description", type: "string"}
		]
	}
});
