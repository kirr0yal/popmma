from django.core import paginator
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from .models import *

NEWS_COUNT_PER_PAGE = 10


def post_list(request):
    page = int(request.GET.get('page', 1))
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    p = paginator.Paginator(posts, NEWS_COUNT_PER_PAGE)

    try:
        post_page = p.page(page)
    except paginator.EmptyPage:
        post_page = paginator.Page([], page, p)

    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        context = {
            'posts': post_page,
            'title': "Последние новости:",
        }
        return render(request, 'main/index.html', context)

    else:
        content = ''
        for post in post_page:
            content += render_to_string('main/post-item.html', {'post': post}, request=request)

        return JsonResponse({
            "content": content,
            "end_pagination": True if page >= p.num_pages else False
        })


# def index(request):
#     posts = Post.objects.filter(is_published=True).order_by("-id")
#     context = {
#         'posts': posts,
#         'title': "Последние новости:"
#     }
#     return render(request, "main/index.html", context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Такой страницы не существует :(</h1>")


def show_post(request, post_slug):
    # post_slug=hfcmma
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        'post': post,
    }
    return render(request, 'main/post.html', context=context)


def show_post_tags(request, tag, slug:str):
    post = get_object_or_404(Post, tag=tag, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'main/post.html', context=context)


def login(request):
    return render(request, "main/login.html")


def show_tags_related_posts(request, tag):
    tag_related_posts = Post.objects.filter(tag=tag)
    context = {
        "posts": tag_related_posts,
        "title": f'News for {tag}'
    }
    return render(request, 'main/index.html', context=context)


