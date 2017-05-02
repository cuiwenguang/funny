# encoding: utf-8
import datetime
from bson import ObjectId

from dictshield.document import Document
from dictshield.fields import *
from dictshield.fields.mongo import ObjectIdField
from dictshield.fields.compound import EmbeddedDocument,EmbeddedDocumentField,ListField

from data.db import articles, favorites


class AuthorDoc(EmbeddedDocument):
    id = StringField(required=True)
    name = StringField(max_length=50, required=True)
    avatar = StringField(max_length=255, required=True)


class ArticleDoc(Document):
    ''' 文章基类 '''
    _id = ObjectIdField()
    title = StringField(min_length=10, max_length=500, required=True)
    category = IntField(required=True) # 文章类型1：文字，2:图片，3:动图,4:视频,5 问答
    channel = IntField(required=True)
    update_time = DateTimeField(default=datetime.datetime.now())
    cover_image = StringField(max_length=255)
    content = StringField(max_length=500)
    html_content = StringField()
    status = IntField(default=0) # 文章状态0：草稿；1：发布；-1：退稿
    user = EmbeddedDocumentField(AuthorDoc)
    tags = ListField(StringField())
    support = ListField(StringField())
    oppose = ListField(StringField())
    share_num = IntField(default=0)
    comment_num = IntField(default=0)


class FavoriteDoc(Document):
    user_id = ObjectIdField()
    article_id = ObjectIdField()


def save(**kwargs):
    article = ArticleDoc(**kwargs)
    if article.validate():
        pk = articles.insert(article.to_python())
        return str(pk)
    else:
        print "%s save error" % article.title
        return None


def remove(pk):
    try:
        articles.delete_one({"_id":ObjectId(pk)})
    except Exception, ex:
        print ex.message


def get_article_by_id(pk):
    artilce = articles.find_one({"_id":ObjectId(pk)})
    return ArticleDoc(**artilce).to_json()


def push(user, channels):
    '''
    获取文章信息
    :param user: 用户
    :param channels 频道集合
    :return: 文章列表
    '''
    return []

def vote(pk, type=1):
    '''
    投票
    :param pk: 文章ID
    :param type: 0，反对，1 支持
    :return:
    '''
    if type == 1:
        articles.update_one({"_id": ObjectId(pk)},{
            "$inc":{
                "support": 1
            }
        })
    elif type == 0 :
        articles.update_one({"_id": ObjectId(pk)}, {
            "$inc": {
                "oppose": 1
            }
        })
    else:
        raise Exception("%s vote error" % pk)


def collect(user_id, article_id):
    '''收藏'''
    favorite = FavoriteDoc(user_id=ObjectId(user_id), article_id=ObjectId(article_id))
    favorites.save(favorite)



