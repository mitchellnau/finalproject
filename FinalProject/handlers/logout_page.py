import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users
from handlers import BaseHandler

class LogoutPage(BaseHandler):
    def get(self):
        # Checks for active Google account session
        user = users.get_current_user()

        if user:
            self.redirect(users.create_logout_url('/loggedout'))
        else:
            self.redirect('/login')

