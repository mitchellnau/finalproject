import webapp2
from google.appengine.api import users
from handlers import BaseHandler

class NewItem(BaseHandler):
    def get(self):
        user = users.get_current_user()
        self.render("new_item.html", {"user": user})
        
        
