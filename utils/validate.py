# encoding: utf-8
import re

def _valid(val, pattern):
    c = re.compile(pattern)
    r = c.match(val)
    if r:
        return True
    else:
        return False


def is_float(val):
    '''
    判断是否为浮点数
    如果只判断是否整数用：val.isdigit()
    :param val:
    :return:
    '''
    pattern = r'^[-+]?[0-9]+\.[0-9]+$'
    return _valid(val, pattern)


def is_version_format(val):
    '''
    版本格式是否正确
    :param val: 版本号
    :return:
    '''
    pattern = r'^v[0-9]{1,2}$'
    return _valid(val, pattern)

