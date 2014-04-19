from django.shortcuts import render
from news.models import Greeting
from django.http import HttpResponse
from services import newsInfo
import json

# Create your views here.

def index(request):
	context = {}
	return render(request, 'index.html',context)

def info(request):
	response_data = {}
	response_data['news'] =  newsInfo()
	return HttpResponse(json.dumps(response_data),content_type="application/json")
