import webapp2
from handlers import BaseHandler

class IndexPage(BaseHandler):
    def get(self):
        self.render("index.html", {})


