# encoding: utf-8

from handlers.home_handler import HomeHandler
from handlers.account_handler import LoginHandler,RegisterHander
from handlers.article_handler import ArticleHandler

urls = [
    (r"/api/register/", RegisterHander),
    (r"/api/login/", LoginHandler),
    (r'/home/(?P<action>\w+)/$', HomeHandler),
    (r'/api/(?P<version>\w+)/articles/(?P<action>\w+)/(?P<id>.*)$', ArticleHandler),
]