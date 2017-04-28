import json
from tornado.web import HTTPError
from tornado.web import RequestHandler

from utils.http import HttpCode
from models.user import UserModel,create_user, login
class LoginHandler(RequestHandler):
    def post(self, *args, **kwargs):
        username = self.get_arguments("username")
        password = self.get_arguments("password")
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
    def post(self, *args, **kwargs):
        email = self.get_argument("email", "")
        password = self.get_argument("password", "")
        username = self.get_argument("username", email)
        if email == "" or password == "":
            raise HTTPError(HttpCode.HTTP_BAD_REQUEST)
        id = create_user(username=username,email=email,password=password)
        self.write(json.dumps({
            "sate": HttpCode.HTTP_SUCCESS,
            "data": id,
        }))
