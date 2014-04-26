from django.shortcuts import render
from django.http import HttpResponse
from google.appengine.ext import ndb
from models import Article
import json
import random

# Create your views here.
def index(request):

	"""
	for i in range(10):
		title = "Vote" + str(i)
		link = "http://bongster.com/" + str(i)
		count = random.randint(100,10000)
		article = Article(title=title,link=link,count = count)
		article.put()
	"""
	if request.method == 'GET':
		response_data = {}
		response_data['vote'] = [a.to_dict() for a in Article.query().order(-Article.count).fetch(20)]
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	elif request.method == 'POST':
		response_data = {}
		response_data['vote'] = [a.to_dict() for a in Article.query().order(-Article.count).fetch(20)]
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		response_data = {}
		response_data['vote'] = [a.to_dict() for a in Article.query().order(-Article.count).fetch(20)]
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	
def delete(request):
	"""
	for i in range(10):
		title = "Vote" + str(i)
		link = "http://bongster.com/" + str(i)
		count = random.randint(100,10000)
		article = Article(title=title,link=link,count = count)
		article.put()
	"""
	if request.method == 'GET':
		response_data = {}
		response_data['method'] = 'delete'
		ndb.delete_multi(Article.query().fetch(keys_only=True))
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	elif request.method == 'POST':
		response_data = {}
		response_data['method'] = 'delete'
		ndb.delete_multi(Article.query().fetch(keys_only=True))
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		response_data = {}
		response_data['method'] = 'delete'
		ndb.delete_multi(Article.query().fetch(keys_only=True))
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	

def like(request):
	if request.method == 'POST':
		response_data = {};
		json_data = json.loads(request.body)
		response_data['result'] = 'true'
		title = json_data['title']
		link = json_data['link']
		article = Article.query(Article.link == link).fetch(1)
		if len(article) is 0:
			newArticle = Article(title=title,link=link,count = 1)
			newArticle.put()
		else:
			article = article[0]
			article.count = article.count + 1
			article.put()
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		response_data = {};
		response_data['result'] = 'false'
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	

def unlike(request):
	if request.method == 'POST':
		response_data = {};
		response_data['result'] = 'true'
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		response_data = {};
		response_data['result'] = 'false'
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	


