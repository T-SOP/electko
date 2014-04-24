from django.shortcuts import render
from django.http import HttpResponse
from models import Article
import json

# Create your views here.
def index(request):

	for i in range(10):
		title = "Vote" + str(i)
		link = "http://bongster.com/" + str(i)
		description = "this is description" + str(i)
		article = Article(title=title,link=link,description=description)
		article.put()

	if request.method == 'GET':
		response_data = {}
		response_data['method'] = 'get'
		response_data['rank'] = Article.query()
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	elif request.method == 'POST':
		response_data = {}
		response_data['method'] = 'post'
		response_data['rank'] = Article.query()
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		response_data = {}
		response_data['method'] = request.method
		response_data['rank'] = Article.query()
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	
	
