# encoding: utf-8
import json

from base_handler import BaseHandler
from utils.http import HttpCode
from models.user import create_user, create_gust, login

class LoginHandler(BaseHandler):
    '''用户登录'''
    def post(self, *args, **kwargs):
        json_data = json.loads(self.request.body)
        username = json_data.get("username", None)
        password = json_data.get("password", None)
        mobile_code = json_data.get('mobile_code', None)
        if username: # 会员
            token =login(username, password)
            if token is None:
                r = {
                    "state": HttpCode.HTTP_UNAUTHORIZED,
                    "data": None,
                    "msg": "Incorrect username or password"
                }
        elif mobile_code: # 游客
            token = create_gust(mobile_code)
            r = {
                "state": HttpCode.HTTP_SUCCESS,
                "data": token,
                "msg": ""
            }
        else:
            r = {
                "state": HttpCode.HTTP_BAD_REQUEST,
                "data": None,
                "msg": "Incorrect username or password or mobile_code"
            }
        self.write(json.dumps(r))


class RegisterHander(BaseHandler):
    '''用户注册'''
    def post(self, *args, **kwargs):
        json_data = json.loads(self.request.body)
        email = json_data.get("email", "")
        password = json_data.get("password", "")
        username = json_data.get("username", email)
        if email == "" or password == "":
            self.write(json.dumps({
                "sate": HttpCode.HTTP_BAD_REQUEST,
                "data": None,
                "msg": "Validation failed"
            }))
        id = create_user(username=username,email=email,password=password)
        self.write(json.dumps({
            "sate": HttpCode.HTTP_SUCCESS,
            "data": id,
        }))


