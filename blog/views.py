from django.shortcuts import render
from blog.models import Blog
from django.core.paginator import Paginator
# Create your views here.


# /
# /index/
def index(request):
    """个人博客首页"""
    # 首页显示最新的6篇文章
    articles = Blog.objects.get_all_article()[:6]
    for a in articles:
        print(a.abstract)

    return render(request, 'blog/index.html', {'list': articles})


# /article_list/(\d+)
def article_list(request, page):
    """文章列表页"""
    articles = Blog.objects.get_all_article()

    # 每页显示8篇文章
    paginator = Paginator(articles, 4)
    result = paginator.page(int(page))

    return render(request, 'blog/article_list.html', {'result': result})


# /article/(\d+)/
def article(request, article_id):
    """文章详情页"""
    # 根据id获取文章
    article_result = Blog.objects.get_one_article_by_id(article_id)
    # 获取上/下一篇文章的名字和id
    next_article, prev_article = Blog.objects.get_page_article(article_id)
    # print(next_article)
    # print(prev_article)
    return render(request, 'blog/article.html', {'article': article_result, 'next': next_article,
                                                 'prev': prev_article})


# /photos/
def photos(request):
    """照片展示"""
    return render(request, 'blog/photos.html')


# /timeline/
def timeline(request):
    """存档时间线"""
    return render(request, 'blog/timeline.html')
