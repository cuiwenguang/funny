# encoding: utf-8
import json

from base_handler import BaseHandler
from utils.http import HttpCode
import models.article


class ArticleHandler(BaseHandler):
    '''文章控制器'''
    def get_detail(self, *args, **kwargs):
        '''获取一篇文章'''
        pk = kwargs.get("id", "")
        if pk == "":
            self.create_response(state=HttpCode.HTTP_BAD_REQUEST, message="id is not null")
        doc = models.article.get_article_by_id(pk)
        self.create_response(data=doc)


    def delete_remove(self, *args, **kwargs):
        '''删除一篇文章'''
        pk = kwargs.get("id", "")
        if pk == "":
            self.create_response(state=HttpCode.HTTP_BAD_REQUEST,
                                 message="id is not null")
        try:
            models.article.remove(pk)
            self.create_response(message="success")
        except:
            self.create_response(state=HttpCode.HTTP_APPLICATION_ERROR)


    def post_create(self, *args, **kwargs):
        '''保存文章'''
        json_data = json.loads(self.request.body)
        pk = models.article.save(**json_data)
        self.create_response(data=pk)


    def post_push(self, *args, **kwargs):
        '''拉取文章'''
        channels = []



    def post_vote(self, *args, **kwargs):
        pk = kwargs.get("id")
        json_data = json.loads(self.request.body)
        type = json_data.get("type", "1")
        try:
            models.article.vote(pk, type)
        except Exception, ex:
            return self.create_response(state=HttpCode.HTTP_APPLICATION_ERROR,
                                        message=ex.message)


    def post_collect(self, *args, **kwargs):
        pk = kwargs.get("id")
        userid = self.current_user["id"]
        try:
            models.article.collect(userid, pk)
            return self.create_response()
        except Exception, ex:
            return self.create_response(state=HttpCode.HTTP_APPLICATION_ERROR,
                                        message=ex.message)


    def post_comment(self, *args, **kwargs):
        pass