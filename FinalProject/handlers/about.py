import webapp2
from handlers import BaseHandler

class About(BaseHandler):
    def get(self):
        self.render("about.html", {})


