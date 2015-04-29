from google.appengine.ext import ndb

class Item(ndb.Model):
	name = ndb.StringProperty(required=True, indexed=True)
	type = ndb.StringProperty(indexed=True)
	description = ndb.TextProperty()
	price = ndb.StringProperty()
	stock = ndb.StringProperty()

