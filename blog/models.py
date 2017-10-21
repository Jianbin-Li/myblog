from django.db import models
from db.base_model import BaseModel
from blog.enums import *


# Create your models here.


class BlogManager(models.Manager):
    """博客模块管理器"""

    def get_all_article(self):
        """获取最新的文章列表"""
        articles = self.filter(is_delete=False).order_by('-pub_time')
        return articles

    def get_all_code_article(self):
        """获取最新的文章列表"""
        articles = self.filter(is_delete=False, type=1).order_by('-pub_time')
        return articles

    def get_all_article_without_code(self):
        """获取最新的文章列表"""
        articles = self.filter(is_delete=False, type__in=[2, 3, 4]).order_by('-pub_time')
        return articles

    def get_one_article_by_id(self, article_id):
        try:
            article = self.get(id=article_id)
        except:
            return None
        else:
            return article

    def get_page_article(self, article_id):
        # 因为是按逆序排列,因此要颠倒
        id_list = self.get_all_article().reverse()
        for temp_index, temp in enumerate(id_list):
            if temp.id == int(article_id):
                next_article = id_list[temp_index + 1] if temp_index != (len(id_list)-1) else None
                prev_article = id_list[temp_index - 1] if temp_index != 0 else None
                return next_article, prev_article


class Blog(BaseModel):
    """个人博客类"""

    def __str__(self):
        return self.title

    article_type_choice = (
        (CODE, ARTICLE_TYPES[CODE]),
        (NOVEL, ARTICLE_TYPES[NOVEL]),
        (ESSAY, ARTICLE_TYPES[ESSAY]),
        (ELSE, ARTICLE_TYPES[ELSE]),
    )
    # 文章名
    title = models.CharField(max_length=50, verbose_name="文章标题")
    # 文章第一段or摘要
    abstract = models.CharField(max_length=512, verbose_name="文章摘要")
    # 文章内容(富文本)
    content = models.TextField(verbose_name="文章内容")
    # 分类
    type = models.SmallIntegerField(
        choices=article_type_choice, default=ELSE, verbose_name='文章分类')
    # 作者 默认是本人
    auth = models.CharField(max_length=24, default='ljb', verbose_name='作者')

    objects = BlogManager()

    class Meta:
        db_table = 'article'


class CommentManager(models.Manager):

    def get_content_by_article_id(self, article_id):
        """根据文章id获取评论内容"""
        try:
            comments = self.filter(article_id=article_id, is_delete=False).order_by('id')
        except:
            comments = None
        return comments

    def add_one_comment(self, article_id, username, email, content):
        """添加一条评论"""
        obj_class = self.model
        try:
            comment = obj_class(article_id=article_id, username=username, email=email, content=content)
            comment.save()
            print(2)
        except:
            comment = None
        else:
            comment = 1

        return comment


class Comment(BaseModel):
    """评论类"""
    article = models.ForeignKey('blog', verbose_name='所属文章')
    username = models.CharField(max_length=20, verbose_name='用户名')
    email = models.EmailField(verbose_name='邮箱')
    content = models.TextField(verbose_name="评论内容")

    objects = CommentManager()

    class Meta:
        db_table = 'comment'

