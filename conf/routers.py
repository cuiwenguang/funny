# encoding: utf-8

from handlers.home_handler import HomeHandler
from handlers.account_handler import LoginHandler,RegisterHander
urls = [
    (r"/api/register", RegisterHander),
    (r"/api/login", RegisterHander),
    (r'^/(?P<version>.*)/home/(?P<action>\w+)/$', HomeHandler),
]