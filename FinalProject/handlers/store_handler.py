import webapp2

from handlers import BaseHandler
from models import Item



class StoreHandler(BaseHandler):
	def get(self):
		items = Item.query().order(-Item.date).fetch(10)
		
		template_values = {
			'items':items
		}
		self.render("store.html", (template_values))
		