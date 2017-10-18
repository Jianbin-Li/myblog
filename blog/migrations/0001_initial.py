# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('pub_time', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='最后修改时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('title', models.CharField(verbose_name='文章标题', max_length=50)),
                ('abstract', models.CharField(verbose_name='文章摘要', max_length=512)),
                ('content', tinymce.models.HTMLField(verbose_name='文章内容')),
                ('type', models.SmallIntegerField(verbose_name='文章分类', default=4, choices=[(1, '代码'), (2, '小说'), (3, '随笔'), (4, '其他')])),
                ('auth', models.CharField(verbose_name='作者', max_length=24, default='ljb')),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
