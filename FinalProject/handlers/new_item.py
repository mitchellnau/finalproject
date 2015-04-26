import webapp2
from handlers import BaseHandler

class NewItem(BaseHandler):
    def get(self):
        self.render("new_item.html", {})
        
        
