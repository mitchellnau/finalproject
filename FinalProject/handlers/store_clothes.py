import webapp2

from handlers import BaseHandler
from models import Item

class StoreClothes(BaseHandler):
	def get(self):
		items = Item.query().filter(Item.type == 'Clothing').order(-Item.date).fetch(10)

		template_values = {
			'items':items
		}
		self.render("clothes.html", (template_values))