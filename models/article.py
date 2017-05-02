# encoding: utf-8
import datetime
from bson import ObjectId

from dictshield.document import Document
from dictshield.fields import *
from dictshield.fields.compound import EmbeddedDocument,EmbeddedDocumentField,ListField

from data.db import articles


class AuthorDoc(EmbeddedDocument):
    id = StringField(required=True)
    name = StringField(max_length=50, required=True)
    avatar = StringField(max_length=255, required=True)


class ArticleDoc(Document):
    ''' 文章基类 '''
    title = StringField(min_length=10, max_length=500, required=True)
    category = IntField(required=True) # 文章类型1：文字，2:图片，3:动图,4:视频
    channel = IntField(required=True)
    update_time = DateTimeField(default=datetime.datetime.now())
    cover_image = StringField(max_length=255)
    content = StringField(max_length=500)
    html_content = StringField()
    status = IntField(default=0) # 文章状态0：草稿；1：发布；-1：退稿
    user = EmbeddedDocumentField(AuthorDoc)
    support = ListField(StringField())
    oppose = ListField(StringField())
    comment_num = IntField(default=0)

def save(**kwargs):
    article = ArticleDoc(**kwargs)


def remove(pk):
    pass

def get_article_by_id(pk):
    pass

def push(user, channels):
    '''
    获取文章信息
    :param user: 用户
    :param channels 频道集合
    :return: 文章列表
    '''
    return []

