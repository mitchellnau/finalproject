from google.appengine.ext import ndb
from google.appengine.api import users

class Task(ndb.Model):
	name = ndb.StringProperty(required=True, indexed = True)
    date = ndb.DateProperty(auto_now_add=True, indexed=True)
	type = ndb.StringProperty(required=True)
	description = ndb.TextProperty()
	creator = ndb.StringProperty()
