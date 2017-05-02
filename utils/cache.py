# encoding: utf-8
import redis

class Cache(object):
    redis = redis.Redis(host="10.20.22.212", port=6379, db=14)

    @classmethod
    def get_cache(cls):
        return cls.redis

    @classmethod
    def get(cls, key, default=None):
        r = cls.redis.get(key)
        if not r:
            r = default
        return r

    @classmethod
    def set(cls, key, value, timeout=0):
        return cls.redis.set(key, value, ex=timeout)

    @classmethod
    def delete(cls, key):
        return cls.redis.delete(key)

    @classmethod
    def flush(cls):
        return cls.redis.flushall()

    def __getattr__(self, key):
        return Cache.get(key)

    def __setattr__(self, key, value):
        return Cache.set(key, value)






