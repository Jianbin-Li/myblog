from django.db import models
from db.base_model import BaseModel
from blog.enums import *
from tinymce.models import HTMLField

# Create your models here.


class BlogManager(models.Manager):
    """博客模块管理器"""

    def get_last_six_article(self):
        """获取最新的6篇文章用于首页展示"""
        articles = self.get_all_article()[:6]
        return articles

    def get_all_article(self):
        """获取最新的文章列表"""
        articles = self.order_by('-pub_time')
        return articles

    def get_one_article_by_id(self, article_id):
        try:
            article = self.get(id=article_id)
        except:
            return None
        else:
            return article


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
    content = HTMLField(verbose_name="文章内容")
    # 分类
    type = models.SmallIntegerField(
        choices=article_type_choice, default=ELSE, verbose_name='文章分类')
    # 作者 默认是本人
    auth = models.CharField(max_length=24, default='ljb', verbose_name='作者')

    objects = BlogManager()

    class Meta:
        db_table = 'article'
