# encoding: utf-8
import functools
from tornado.web import HTTPError
def authenticated(method):
    """
    api 接口授权认证的过滤器
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            raise HTTPError(401)
        return method(self, *args, **kwargs)
    return wrapper