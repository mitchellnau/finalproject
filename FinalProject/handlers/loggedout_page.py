import webapp2
from google.appengine.api import users
from handlers import BaseHandler

class LoggedOutPage(BaseHandler):
    def get(self):
        user = users.get_current_user()
        self.render("loggedout.html", {"user": user})


