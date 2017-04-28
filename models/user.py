import datetime
import hashlib
import bson
from dictshield.document import Document
from dictshield.fields import StringField,IntField,EmailField,MD5Field, BooleanField,DateTimeField

from utils.auth import token_encode
from data.db import mongo,users
from conf.settings import SECRET_KEY


class UserModel(Document):
    username = StringField(max_length=50)
    email = EmailField(max_length=50)
    password = MD5Field(required=False)
    is_active = BooleanField(default=True)
    avatar = StringField(max_length=255)
    create_time = DateTimeField(default=datetime.datetime.now())
    last_login_time = DateTimeField(default=datetime.datetime.now())

def make_pwd(pwd):
    md5 = hashlib.md5(pwd+SECRET_KEY)
    return md5.hexdigest()

def create_user(username, email, password=None):
    user = UserModel(username=username, email=email)
    result = users.find_one({"$or": [{"username": username}, {"emial": username}]})
    if result is not None:
        raise Exception("username or email is exits")
    if password is not None:
        user.password = make_pwd(pwd=password)
    id = users.insert(user.to_python())
    token = token_encode(str(id))
    return token

def login(username, password):
    result = users.find_one({"$or":[{"username":username},{"emial":username}]})
    user = UserModel(result)
    if make_pwd(password) == user.password:
        return user
    else:
        return None
