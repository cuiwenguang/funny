# encoding: utf-8
import datetime

from dictshield.document import Document
from dictshield.fields import *
from dictshield.fields.mongo import ObjectIdField
from dictshield.fields.compound import EmbeddedDocument, EmbeddedDocumentField

from article import AuthorDoc


class ReplyDoc(EmbeddedDocument):
    _id = ObjectIdField()
    user = EmbeddedDocumentField(AuthorDoc)
    content = StringField(max_length=500)
    update_time = DateTimeField(default=datetime.datetime.now())


class CommentDoc(Document):
    _id = ObjectIdField()
    content = StringField(max_length=500)
    user = EmbeddedDocumentField(AuthorDoc)
    update_time = DateTimeField(default=datetime.datetime.now())
    reply = EmbeddedDocumentField(ReplyDoc)
    is_best = BooleanField(default=False) # 最佳评论，如果是问答，表示被采用
    article_id = StringField(required=True) # 文章ＩＤ