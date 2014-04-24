from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
	if request.method is "POST":
		response_data = {}
		response_data['method'] = 'post'
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	elif request.method is "GET":
		response_data = {}
		response_data['method'] = 'get'
		return HttpResponse(json.dumps(response_data),content_type="application/json")
