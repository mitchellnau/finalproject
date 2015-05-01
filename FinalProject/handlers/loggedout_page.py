import webapp2
from handlers import BaseHandler

class LoggedOutPage(BaseHandler):
    def get(self):
        self.render("loggedout.html", {})


