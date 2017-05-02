import tornado.web
from base_handler import BaseHandler
from utils.filter.auth import authenticated
class HomeHandler(BaseHandler):
    @authenticated
    def get_index(self, *args, **kwargs):
        self.write("hello world")