from django.db import models

from google.appengine.ext import ndb

class Article(ndb.Model):
	title = ndb.StringProperty(indexed=False)
	description = ndb.StringProperty(indexed=False)
	link = ndb.StringProperty()

class Ranks(ndb.Model):
	rank = ndb.IntegerProperty()
	article = ndb.StructuredProperty(Article)
