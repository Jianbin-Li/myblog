from django.shortcuts import render
from blog.models import Blog, Comment
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.


# /
# /index/
def index(request):
    """个人博客首页"""
    # 首页显示最新的6篇文章
    articles = Blog.objects.get_all_article()[:6]
    return render(request, 'blog/index.html', {'list': articles})


# /article_list/(\d+)
def article_list(request, page):
    """文章列表页"""
    articles = Blog.objects.get_all_article_without_code()

    # 每页显示8篇文章
    paginator = Paginator(articles, 4)
    result = paginator.page(int(page))

    return render(request, 'blog/article_list.html', {'result': result})


# /article_list/(\d+)
def code_list(request, page):
    """文章列表页"""
    articles = Blog.objects.get_all_code_article()

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
    # 根据id获取评论
    comments = Comment.objects.get_content_by_article_id(article_id)
    # 如果comments为空字符串 也返回None
    if len(comments) == 0:
        comments = None

    return render(request, 'blog/article.html', {'article': article_result, 'next': next_article,
                                                 'prev': prev_article, 'comments': comments})


# /comment
def add_comment(request):
    """增加评论"""
    article_id = request.POST.get('article_id')
    username = request.POST.get('username')
    email = request.POST.get('email')
    content = request.POST.get('content')
    # print(article_id)
    # print(username, email, content)
    # 添加评论
    comment = Comment.objects.add_one_comment(article_id=article_id, username=username, email=email, content=content)
    print(comment)
    if comment is None:
        return JsonResponse({'data': 0})
    else:
        next_url = '/article/{}'.format(article_id)
        return JsonResponse({'data': 1, 'next_url': next_url})


# /photos/
def photos(request):
    """照片展示"""
    return render(request, 'blog/photos.html')


# /timeline/
def timeline(request):
    """存档时间线"""
    return render(request, 'blog/timeline.html')
