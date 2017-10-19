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


class ArticleImageManager(models.Manager):
    pass


class ArticleImage(BaseModel):
    """文章包含的图片类"""
    article = models.ForeignKey('Blog', verbose_name='所属商品')
    img_url = models.ImageField(upload_to='blog', verbose_name='文章图片')
    img_name = models.CharField(max_length=20, verbose_name='图片名称')

    objects = ArticleImageManager()

    def __str__(self):
        return self.img_name

    class Meta:
        db_table = "image"
