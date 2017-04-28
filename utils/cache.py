# encoding: utf-8
import memcache
from conf.settings import APP_CONFIG

class Cache(object):
    cache_config = getattr(APP_CONFIG, 'CACHES')
    cache_name = cache_config['default']
    _mc = memcache.Client(cache_config[cache_name]['url'], debug=cache_config[cache_name]['debug'])

    @classmethod
    def get_cache(cls):
        return cls._mc

    @classmethod
    def get(cls, key, default=None):
        r = cls._mc.get(key)
        if not r:
            r = default
        return r

    @classmethod
    def set(cls, key, value, timeout=0):
        return cls._mc.set(key, value, timeout)

    @classmethod
    def delete(cls, key):
        return cls._mc.delete(key)

    @classmethod
    def flush(cls):
        return cls._mc.flush_all()

    def __getattr__(self, key):
        return Cache.get(key)

    def __setattr__(self, key, value):
        return Cache.set(key, value)






