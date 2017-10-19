from django.contrib import admin
from blog.models import Blog

# Register your models here.
from django.contrib import admin
from .models import *
from pagedown.widgets import AdminPagedownWidget
from django import forms
# Register your models here.
# 定义自己的form


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())
    # 注意此处的content就是markdown编辑器所在，但不会保存数据，只供预览

    class Meta:
        model = Blog
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm


# class ArticleImageAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Blog, ArticleAdmin)
admin.site.register(ArticleImage)
