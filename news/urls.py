from django.conf.urls import patterns, url
from news import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^info$', views.info, name='info'),
		url(r'^update$', views.update, name='update'),
)

