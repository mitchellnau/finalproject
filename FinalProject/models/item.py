from google.appengine.ext import ndb

class Item(ndb.Model):
	name = ndb.StringProperty(required=True)
	#Can use queries on type property
	type = ndb.StringProperty()
	description = ndb.TextProperty()
	#Can change to integer if needed, can use Amazon or Paypal to handle money
	price = ndb.FloatProperty()
	stock = ndb.IntegerProperty()
	#Potential Others: Reviews , image , rating ,also tags for the search
