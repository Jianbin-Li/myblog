from django.db import models


class BaseModel(models.Model):
    """模型类基类"""
    # 发布时间
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    # 修改时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")
    # 删除标记
    is_delete = models.BooleanField(default=False, verbose_name="删除标记")

    class Meta:
        abstract = True
