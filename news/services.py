#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import urllib
from lxml import etree as ET
import collections
import re

class Rss:
	def __init__(self,url,newsList):
		self.url = url
		self.newsList = newsList
		print newsList
#		self.xml = urllib2.urlopen(url).read().decode('cp949','ignore').encode('utf-8')

def newsInfo():
	infos = []
	url = 'http://tab.search.daum.net/dsa/search?w=news&m=rss&SortType=1&q=%B9%DA%BF%F8%BC%F8&cp=37730750'
	rss = Rss(url,["37736525","70640889,264","1119","120","78305928"])
	data = {}
	data['q'] = '박원순'
	print data['q']
	data['cp'] = '37730750'
#	req = urllib2.Request(url,data)
	response = urllib2.urlopen(url)
	xml =  response.read().decode('cp949', 'ignore').encode('utf-8')
	parser = ET.XMLParser(encoding="utf-8")
	rss =  ET.fromstring(xml,parser = parser)

	items = rss.findall('.//channel/item')
	info = {}
	for item in items:
		info['title'] = item.find('title').text
		info['link'] = item.find('link').text
		info['content'] = child(item.find('link').text)
		infos.append(info)

	return infos

def child(url):
	print url
	response =	urllib2.urlopen(url).read()
	parser = ET.HTMLParser()
	tree = ET.fromstring(response,parser)
	newsbody = tree.find(".//h4[@id='newsBodyShadow']")
	if newsbody is None:
		newsbody = tree.find(".//div[@id='newsBody']")
	brace_re = '[\[\{\(].*?[\]\}\)]|[\']';
	email_re = '[^@]+@[^@]+\.[^@]+' 
	default_news = ET.tostring(newsbody,method="text",encoding="utf-8")
	no_brace_news = re.sub(brace_re,'',default_news)
	return no_brace_news

def wordCount(words,splitword = ' '):
	return collections.Counter(words.split(splitword))
