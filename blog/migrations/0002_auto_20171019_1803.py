# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('img_url', models.ImageField(verbose_name='文章图片', upload_to='blog')),
                ('img_name', models.CharField(max_length=20, verbose_name='图片名称')),
            ],
            options={
                'db_table': 'image',
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name='文章内容'),
        ),
        migrations.AddField(
            model_name='articleimage',
            name='article',
            field=models.ForeignKey(to='blog.Blog', verbose_name='所属商品'),
        ),
    ]
