from django.db import models

from google.appengine.ext import ndb

class Article(ndb.Model):
	title = ndb.StringProperty(indexed=False)
	count = ndb.IntegerProperty()
	link = ndb.StringProperty()
