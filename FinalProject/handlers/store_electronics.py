import webapp2

from handlers import BaseHandler
from models import Item

class StoreElectronics(BaseHandler):
	def get(self):
		items = Item.query().filter(Item.type == 'Electronics').order(-Item.date).fetch(10)

		template_values = {
			'items':items
		}
		self.render("store.html", (template_values))