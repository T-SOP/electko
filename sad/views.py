from django.shortcuts import render

def sencha_home(request):
	return render(request,'sencha.html',{})

def angular_home(request):
	return render(request,'angular.html',{})
