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


def jwtauth(handler_execute):
    ''' jwt装饰器 '''
    def wrap_execute(handler_execute):
        def require_auth(handler, kwargs):

            auth = handler.request.headers.get('Authorization')
            if auth:
                parts = auth.split()

                if parts[0].lower() != 'bearer':
                    handler._transforms = []
                    handler.set_status(401)
                    handler.write("invalid header authorization")
                    handler.finish()
                elif len(parts) == 1:
                    handler._transforms = []
                    handler.set_status(401)
                    handler.write("invalid header authorization")
                    handler.finish()
                elif len(parts) > 2:
                    handler._transforms = []
                    handler.set_status(401)
                    handler.write("invalid header authorization")
                    handler.finish()

                token = parts[1]
                try:
                    jwt.decode(
                        token,
                        SECRET_KEY,
                        options=options
                    )

                except Exception, e:
                    handler._transforms = []
                    handler.set_status(401)
                    handler.write(e.message)
                    handler.finish()
            else:
                handler._transforms = []
                handler.write("Missing authorization")
                handler.finish()

            return True

        def _execute(self, transforms, *args, **kwargs):

            try:
                require_auth(self, kwargs)
            except Exception:
                return False

            return handler_execute(self, transforms, *args, **kwargs)

        return _execute

    return handler_execute

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
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def token_decode(token):
    return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])