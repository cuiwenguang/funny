# encoding: utf-8
import datetime
import hashlib
import uuid
import bson

from dictshield.document import Document
from dictshield.fields.mongo import ObjectIdField
from dictshield.fields import StringField,IntField,EmailField,MD5Field, BooleanField,DateTimeField
from dictshield.fields.compound import ListField

from utils.cache import Cache
from utils.token import token_encode
from data.db import mongo,users
from conf.settings import SECRET_KEY

class RoleDoc(Document):
    role_name = StringField(required=True)
    role_seq = IntField(required=True)

class UserDoc(Document):
    '''用户'''
    _id = ObjectIdField()
    username = StringField(max_length=50)
    email = EmailField(max_length=50, default="")
    password = MD5Field(default="")
    is_active = BooleanField(default=True)
    is_gust = BooleanField(default=True)
    roles = ListField(IntField(),default=[1])
    avatar = StringField(max_length=255)
    create_time = DateTimeField(default=datetime.datetime.now())
    last_login_time = DateTimeField(default=datetime.datetime.now())
    language = StringField(default='en')
    country = StringField(max_length=20)
    mobile_code = StringField(max_length=50) #手机识别码
    mobile_brand = StringField(max_length=20) # 手机品牌
    mobile_number = StringField(max_length=20) # 手机号码
    provider = StringField(default='local') # 认证方式
    open_id = StringField() # 第三方登录id


def make_pwd(pwd):
    md5 = hashlib.md5(pwd+SECRET_KEY)
    return md5.hexdigest()


def create_user(username, email, mobile_code="", password=None):
    user = UserDoc(username=username, email=email, is_gust=False, mobile_code=mobile_code)
    result = users.find_one({"$or": [{"username": username}, {"emial": username}]})
    if result is not None:
        raise Exception("username or email is exits")
    if password is not None:
        user.password = make_pwd(pwd=password)
    id = users.insert(user.to_python())
    token = token_encode(str(id))
    return token


def create_gust(mobile_code):
    user = users.find_one({"$and": [{"mobile_code": mobile_code},{"is_gust": True}]})
    if user:
        return token_encode(str(user["_id"]))
    user = UserDoc(username=uuid.uuid1(), email="", mobile_code=mobile_code)
    pk = users.save(user.to_python())
    return token_encode(str(id))


def login(username, password):
    result = users.find_one({"$or":[{"username":username},{"emial":username}]})
    user = UserDoc(**result)
    if make_pwd(password) == user.password:
        return user
    else:
        return None


def get_user(pk):
    user = users.find_one(
        {"_id": bson.ObjectId(pk)}
    )
    user = UserDoc(**user).to_json()
    return user

    '''
    user = Cache.get(pk)
    if user:
        return user
    user = users.find_one(
        {"_id": bson.ObjectId(pk)}
    )
    user = UserDoc(**user).to_json()
    if user is None:
        raise  Exception('error token')
    Cache.set(pk, user)
    return user
    '''

