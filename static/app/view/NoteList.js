Ext.define('Sencha.view.NoteList',{
	extend: 'Ext.dataview.List',
xtype: 'notelist',
config: {
		itemTpl: '{title} [{author} <br /> {link} <br /> {description}',
		store : 'News',
		onItemDisclosure: function(record,btn,index){
		
		}
}
});
