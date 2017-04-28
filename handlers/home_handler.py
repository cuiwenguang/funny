import tornado.web
from base_handler import BaseHandler

class HomeHandler(BaseHandler):
    def get(self):
        self.write("hello world")