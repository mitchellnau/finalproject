import webapp2
from models import Item
from handlers import BaseHandler

class ItemInput(webapp2.RequestHandler):
	def post(self):
		#Getting Inputs
		itemname=self.request.get("item_name")
		itemtype=self.request.get("item_type")
		itemdescription=self.request.get("item_description")
		itemprice=self.request.get("item_price")
		itemstock=self.request.get("item_stock")
		
		
		#Placing data in model
		item=Item()
		item.name=itemname
		item.type=itemtype
		item.description=itemdescription
		item.price=itemprice
		item.stock=itemstock
		
		item.put()
		self.response.out.write("Details entered into the datastore")