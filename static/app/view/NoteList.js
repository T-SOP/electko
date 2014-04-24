Ext.define('Sencha.view.NoteList',{
	extend: 'Ext.dataview.List',
xtype: 'notelist',
config: {
		store : 'Note',
		itemTpl: [
						'<div>',
							'<div>{title}</div>',
							'<p>{description}</p>',
						'</div>'
					],
		onItemDisclosure: function(record,btn,index){
		
		}
}
});
