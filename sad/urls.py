from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^news/', include('news.urls')),
    url(r'^vote/', include('vote.urls')),
		url(r'^sencha', 'sad.views.sencha_home',name="home"),
		url(r'^angular', 'sad.views.angular_home',name="home"),
)
