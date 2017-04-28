# encoding: utf-8

from handlers.home_handler import HomeHandler
from handlers.account_handler import LoginHandler,RegisterHander
urls = [
    (r"/", HomeHandler),
    (r"/register", RegisterHander)
]