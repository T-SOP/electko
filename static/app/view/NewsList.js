Ext.define('Ext.view.NewsList',{
	extend: 'Ext.dataview.List',
	xtype: 'newsListView',
	config: {
	id: 'newsList',
	itemTpl: '{title} [{author} <br /> {link} <br /> {description}',
	grouped: true,
	indexBar: true,
	infinite: true,
	useSimpleItems: true,
	variableHeights: true,
	striped: true,
	ui: 'round',
	store : 'News'
	}
});
