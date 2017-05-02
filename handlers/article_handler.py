# encoding: utf-8
import json

from base_handler import BaseHandler
from utils.http import HttpCode
import models.article


class ArticleHandler(BaseHandler):
    '''文章控制器'''
    def get_article(self, *args, **kwargs):
        '''获取一篇文章'''
        id = kwargs.get("id", "")
        if id == "":
            self.create_response(state=HttpCode.HTTP_BAD_REQUEST, message="id is not null")
        doc = models.article.get_article_by_id(id)
        self.create_response(data=doc)

    def delete_article(self, *args, **kwargs):
        '''删除一篇文章'''
        id = kwargs.get("id", "")
        if id == "":
            self.create_response(state=HttpCode.HTTP_BAD_REQUEST,message="id is not null")
        try:
            models.article.remove(id)
            self.create_response(message="success")
        except:
            self.create_response(state=HttpCode.HTTP_APPLICATION_ERROR)

    def post_create(self, *args, **kwargs):
        '''保存一盘文章'''
        json_data = json.loads(self.request.body)
        article = models.article.save(**json_data)
        pk = article.save()
        self.create_response(data=pk)

    def get_articles(self, *args, **kwargs):
        '''获取某一频道的文章'''
        pass

    def post_list(self, *args, **kwargs):
        '''拉取文章'''
        pass