# encoding: utf-8

from tornado.web import RequestHandler, HTTPError

from utils.http import HttpCode
from utils.serialize import to_json

class BaseHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.set_header('Content-Type', 'application/json')
        if self.settings['allow_remote_access']:
            self.access_control_allow()

    def get_current_user(self):
        '''
        重写 该方法，通过令牌从缓冲中获取当前用户数据
        :return:
        '''
        auth_header = self.request.headers.get_list('AUTHORIZATION')
        if 0 < len(auth_header):
            token = auth_header[0].split(' ')[1]
            return {}
        else:
            return None

    def access_control_allow(self):
        # 允许 JS 跨域调用
        self.set_header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Depth, User-Agent, X-File-Size, "
                                                        "X-Requested-With, X-Requested-By, If-Modified-Since, "
                                                        "X-File-Name, Cache-Control, Token")
        self.set_header('Access-Control-Allow-Origin', '*')

    def create_response(self, data=None, state=HttpCode.HTTP_SUCCESS, message=''):
        result = {
            "state": state,
            "data": data,
            "msg": message
        }
        self.write(to_json(result))


    def get(self, *args, **kwargs):
        '''
        默认的get处理方式，作为所有个头操作根据规则路由到相应的方法中
        :param args:
        :param kwargs:
        :return:
        '''
        f = self._get_func('get', *args, **kwargs)
        f(*args, **kwargs)


    def post(self, *args, **kwargs):
        '''
        默认的post 操作,分发给相应的处理函数
        :param args:
        :param kwargs:
        :return:
        '''
        f = self._get_func('post', *args, **kwargs)
        f(*args, **kwargs)

    def delete(self, *args, **kwargs):
        '''
        默认的delete 操作,分发给相应的处理函数
        :param args:
        :param kwargs:
        :return:
        '''
        f = self._get_func('delete', *args, **kwargs)
        f(*args, **kwargs)

    def _get_func(self, method, *args, **kwargs):
        v = kwargs['version']
        action = kwargs["action"]
        # func_name = method + '_' + v + "_" + action
        try:
            func_name = method + "_" + v + "_" + action
            func = getattr(self, func_name)
        except:
            try:
                func_name = method + "_" + action
                func = getattr(self, func_name)
            except AttributeError:
                print ArithmeticError.message
                raise HTTPError(HttpCode.HTTP_NOT_FOUND)
        return func
