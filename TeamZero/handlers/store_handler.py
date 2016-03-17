import webapp2
from google.appengine.api import users
from handlers import BaseHandler
from models import Item



class StoreHandler(BaseHandler):
	def get(self):
		user = users.get_current_user()
		items = Item.query().order(-Item.date).fetch(10)     
		
		template_values = {
			'items':items,
            'user': user
		}
		self.render("store.html", (template_values))
		
