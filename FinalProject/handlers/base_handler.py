import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    extensions=['jinja2.ext.autoescape'],
    loader=jinja2.FileSystemLoader(
        os.path.dirname(__file__) + "/../templates"),
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):       #Handlers are roughly equivalent to controllers in MVC

    def __init__(self, request=None, response=None):
        super(BaseHandler, self).__init__(request, response)
        # your own code goes here...

    def render(self, template_name, template_values):
        template = jinja_environment.get_template(template_name)
        self.response.out.write(template.render(template_values))
