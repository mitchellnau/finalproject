import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users
from handlers import BaseHandler

class SplashPage(BaseHandler):
    def get(self):
        user = users.get_current_user()
        template_values = {}
        if user:
            url = users.create_logout_url('/')
            url_linktext = 'Logout'
            greeting = "Goodbye, "
        else:
            url = users.create_login_url('/main')
            url_linktext = 'Login'
            greeting = "Hello, you."

        self.render("splash.html", {
          'greetings': greeting ,
          'user': user,
          'url': url,
          'url_linktext': url_linktext
        })