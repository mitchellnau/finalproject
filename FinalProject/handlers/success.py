import webapp2
from handlers import BaseHandler

class Success(BaseHandler):
    def get(self):
        self.render("success.html", {})


