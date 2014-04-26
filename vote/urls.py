from django.conf.urls import patterns, url
from vote import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^like$', views.like, name='like'),
		url(r'^unlike$', views.unlike, name='unlike'),
		url(r'^delete$', views.delete, name='delete'),
)

