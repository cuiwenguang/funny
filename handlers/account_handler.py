import json
from tornado.web import HTTPError

from base_handler import BaseHandler
from utils.http import HttpCode
from models.user import create_user, login

class LoginHandler(BaseHandler):
    def post(self, *args, **kwargs):
        json_data = json.loads(self.request.body)
        username = json_data.get("username", "")
        password = json_data.get("password", "")
        user =login(username, password)
        if user is None:
            self.create_response(state=HttpCode.HTTP_UNAUTHORIZED,
                                 message="Incorrect username or password")
        else:
            self.create_response(data=user)

class RegisterHander(BaseHandler):
    def post(self, *args, **kwargs):
        json_data = json.loads(self.request.body)
        email = json_data.get("email", "")
        password = json_data.get("password", "")
        username = json_data.get("username", email)
        if email == "" or password == "":
            raise HTTPError(HttpCode.HTTP_BAD_REQUEST)
        try:
            token = create_user(username=username,email=email,password=password)
            self.create_response(data=token)
        except Exception, ex:
             self.create_response(state=HttpCode.HTTP_BAD_REQUEST,message=ex.message)
