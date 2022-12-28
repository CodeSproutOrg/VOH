from django.http import HttpResponseNotFound
from django.shortcuts import render

from .forms import UserPostForm
from .models import Post, Link


def index(request):
    data = {"title": "Voices of Hope"}
    return render(request, "pages/main.html", context=data)


def posts(request):
    data = {"title": "Posts", "posts": Post.objects.all()}
    return render(request, "pages/posts.html", context=data)


def stories(request):
    form = UserPostForm()
    data = {"title": "Posts", 'form': form}
    if request.method == "POST":
        new_post = UserPostForm(request.POST)
        if new_post.is_valid():
            new_post.save()
            return render(request, 'pages/stories.html', context=data)
    return render(request, "pages/stories.html", context=data)


def links(request):
    data = {"title": "Links of Hope", 'links': Link.objects.all()}
    return render(request, "pages/links.html", context=data)


def help_us(request):
    data = {"title": "Help Us"}
    return render(request, "pages/help-us.html", context=data)


def pageNotFound(request, exception):
    data = {"title": "Ops, something is wrong"}
    return render(request, "pages/error.html", context=data)
