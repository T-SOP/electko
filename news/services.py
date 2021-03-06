#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import urllib
from lxml import etree as ET
import collections
import re
import logging

class Rss:
	def __init__(self,url,newsList):
		self.url = url
		self.newsList = newsList
		print newsList
#		self.xml = urllib2.urlopen(url).read().decode('cp949','ignore').encode('utf-8')

def newsInfo():
	infos = []
#	url = 'http://tab.search.daum.net/dsa/search?w=news&m=rss&SortType=1&q=%EC%84%B8%EC%9B%94%ED%98%B8&'
	url = 'http://tab.search.daum.net/dsa/search?w=news&m=rss&SortType=1&'
	cps = ["37736525","70640889,264","1119","120","78305928","1185","73","98","23","310","49","8"]
	for cp in cps:
		data = {}
		data['q'] = '세월호'
#		data['cp'] = cp
		data = urllib.urlencode(data)
		req = urllib2.Request(url,data)
		response = urllib2.urlopen(req)
		xml =  response.read().decode('cp949', 'ignore').encode('utf-8')
		parser = ET.XMLParser(encoding="utf-8")
		rss =  ET.fromstring(xml,parser = parser)
		print xml
		items = rss.findall('.//channel/item')
		for item in items:
			info = {};
			info['title'] = item.find('title').text
			info['link'] = item.find('link').text
			info['author'] = item.find('author').text
	#		info['description'] = item.find('description').text
	#		info['content'] = child(item.find('link').text)
			infos.append(info)
	print infos
	return infos

def child(url):
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

if __name__ == "__main__":
	print newsInfo()
