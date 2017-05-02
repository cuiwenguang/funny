# encoding: utf-8
import base64,datetime
import jwt

from conf.settings import SECRET_KEY

options = {
    'verify_signature': True,
    'verify_exp': True,
    'verify_nbf': False,
    'verify_iat': True,
    'verify_aud': False
}

def token_encode(id, seconds=3600):
    # jwt 荷载
    current_time = datetime.datetime.utcnow()
    expire_time = current_time + datetime.timedelta(seconds=seconds)
    payload = {
        "sub": "1",
        "iss": "/auth/login",
        "iat": current_time,
        "exp": expire_time,
        "nbf": current_time,
        "jti": id
    }
    return jwt.encode(payload,SECRET_KEY, algorithm='HS256')

def token_decode(token):
    return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])