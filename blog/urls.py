from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$', views.index),  # 博客首页
    url(r'^index/$', views.index),
    url(r'^article/(\d+?)/$', views.article),  # 代码文章之外的列表页
    url(r'^article_list/(\d+?)', views.article_list),  # 文章列表页
    url(r'^code_list/(\d+?)', views.code_list),  # 代码列表页
    url(r'^photos/$', views.photos),  # 图片库
    url(r'^timeline/$', views.timeline),  # 存档时间线
    url(r'^comment/$', views.add_comment),  # 增加评论

]
