import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users
from handlers import BaseHandler

class LoginPage(BaseHandler):
    def get(self):
        # Checks for active Google account session
        user = users.get_current_user()

        if user:
            self.redirect('/loggedin')
        else:
            self.redirect(users.create_login_url(self.request.uri))


    """
    def get(self):
        user = users.get_current_user()
        template_values = {}
        if user:
            url = users.create_logout_url('/')
            url_linktext = 'Logout'
            greeting = "Goodbye, "
        else:
            url_linktext = 'Login'
            greeting = "Hello, you."
            url = '/'
            self.redirect(users.create_login_url(self.request.uri))

        self.render("splash.html", {
          'greetings': greeting ,
          'user': user,
          'url': url,
          'url_linktext': url_linktext
        })
"""
