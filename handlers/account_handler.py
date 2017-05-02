# encoding: utf-8
import json
from tornado.web import HTTPError
from tornado.web import RequestHandler

from utils.http import HttpCode
from models.user import create_user, login

class LoginHandler(RequestHandler):
    '''用户登录'''
    def post(self, *args, **kwargs):
        username = self.get_body_arguments("username")
        password = self.get_body_arguments("password")
        user =login(username, password)
        if user is None:
            r = {
                "state": HttpCode.HTTP_UNAUTHORIZED,
                "data": None,
                "msg": "Incorrect username or password"
            }
        else:
            r = {
                "state": HttpCode.HTTP_SUCCESS,
                "data": user,
                "msg": ""
            }
        self.write(json.dumps(r))


class RegisterHander(RequestHandler):
    '''用户注册'''
    def post(self, *args, **kwargs):
        json_data = json.loads(self.request.body)
        email = json_data.get("email", "")
        password = json_data.get("password", "")
        username = json_data.get("username", email)
        if email == "" or password == "":
            raise HTTPError(HttpCode.HTTP_BAD_REQUEST)
        id = create_user(username=username,email=email,password=password)
        self.write(json.dumps({
            "sate": HttpCode.HTTP_SUCCESS,
            "data": id,
        }))
