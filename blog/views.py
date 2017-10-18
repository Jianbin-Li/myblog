from django.shortcuts import render
from blog.models import Blog
# Create your views here.


# /
# /index/
def index(request):
    """个人博客首页"""
    articles = Blog.objects.get_last_six_article()
    return render(request, 'blog/index.html', {'six_list': articles})


# /article/(\d+)/
def article(request, article_id):
    """文章详情页"""
    # 根据id获取文章
    article = Blog.objects.get_one_article_by_id(article_id)
    return render(request, 'blog/article.html', {'article': article})


# /photos/
def photos(request):
    """照片展示"""
    return render(request, 'blog/photos.html')


# /timeline/
def timeline(request):
    """存档时间线"""
    return render(request, 'blog/timeline.html')