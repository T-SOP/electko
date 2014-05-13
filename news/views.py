from django.shortcuts import render
from news.models import Greeting
from google.appengine.api import users, memcache
from django.http import HttpResponse
from services import newsInfo
import json

# Create your views here.

def index(request):
	context = {}
	context['imageUrl'] = 'http://nec.go.kr';
	return render(request, b'index.html',context)

def info(request):
	info = memcache.get('news')
	if info is not None:
		response_data = {}
		response_data['news'] = info
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		response_data = {}
		news = newsInfo()
		response_data['news'] = news
		memcache.add('news',news)
		return HttpResponse(json.dumps(response_data),content_type="application/json")

def update(request):
	info = memcache.get('news')
	news = newsInfo()
	response_data= {}
	if info is not None:
		response_data['status']= 'update'
		memcache.replace('news',news)
	else:
		response_data['status']= 'create'
		memcache.add('news',news)

	return HttpResponse(json.dumps(response_data),content_type="application/json")
	
	


