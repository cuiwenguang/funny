# encoding: utf-8
import json, datetime

class CJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.strftime('%x')
        elif isinstance(o, datetime.datetime):
            return o.strftime('%X')
        else:
            return json.JSONEncoder.default(self, o)


def to_json(data):
    return json.dumps(data, cls=CJsonEncoder)

def to_dict(str):
    '''
    hook:转对象前,特殊类型字段处理预留
    '''
    return json.loads(str)