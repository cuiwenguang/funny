# encoding: utf-8

# app 启动设置
settings = {
    "template_path": 'templates',
    "allow_remote_access": True,
    "debug": True
}

mongo = {
    "url": "mongodb://10.20.22.131/FunDB"
}

SECRET_KEY = "funny_secret_key_test"

CHANNELS = [
    {
        "id": 1,
        "name": "Joke",
    },
    {
        "id": 2,
        "name": "Memes"
    },
    {
        "id": 3,
        "name": "Vedio"
    }
]