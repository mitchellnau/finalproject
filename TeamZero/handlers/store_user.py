import webapp2
from google.appengine.api import users
from handlers import BaseHandler
from models import Item

class StoreUser(BaseHandler):
	def get(self):
		user = users.get_current_user()
		items = Item.query().filter(Item.owner == user.email()).order(-Item.date).fetch(10)

		template_values = {
			'items':items,
                        'user':user
		}
		self.render("user_store.html", (template_values))
