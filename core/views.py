from django.shortcuts import render
from .models import Post


def index(request):
    data = {"title": "Voices of Hope"}
    return render(request, "pages/main.html", context=data)


def posts(request):
    data = {"title": "Posts", "posts": Post.objects.all()}
    return render(request, "pages/posts.html", context=data)


def links(request):
    data = {"title": "Links of Hope"}
    return render(request, "pages/links.html", context=data)


def help_us(request):
    data = {"title": "Help Us"}
    return render(request, "pages/help-us.html", context=data)

