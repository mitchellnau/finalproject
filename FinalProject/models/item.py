from google.appengine.ext import ndb
from google.appengine.api import users

class Item(ndb.Model):
	name = ndb.StringProperty(required=True, indexed=True)
	type = ndb.StringProperty(indexed=True)
	description = ndb.TextProperty()
	price = ndb.StringProperty()
	stock = ndb.StringProperty()
	date = ndb.DateProperty(auto_now_add=True)
	owner = ndb.StringProperty()
