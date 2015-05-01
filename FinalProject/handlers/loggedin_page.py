import webapp2
from handlers import BaseHandler

class LoggedInPage(BaseHandler):
    def get(self):
        self.render("loggedin.html", {})


