import logging
from django.shortcuts import render, redirect

from .forms import UserPostForm
from .models import Post, Link
from .mail_notification import new_story_notification, signing_up_for_an_online_group_notification

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(funcName)s - %(message)s",
    handlers=[logging.FileHandler('./server.log', encoding='utf-8')]
)
logger = logging.getLogger(__name__)


def index(request):
    form = UserPostForm()
    data = {"title": "Voices of Hope", "forms": form}
    if request.method == 'POST':
        email = request.POST.get('email')
        signing_up_for_an_online_group_notification(email)
        return render(request, "pages/main.html", context=data)
    return render(request, "pages/main.html", context=data)


def links(request):
    data = {"title": "Links of Hope", 'links': Link.objects.all()}
    return render(request, "pages/links.html", context=data)


def posts(request):
    data = {"title": "Posts", "posts": Post.objects.all()}
    return render(request, "pages/posts.html", context=data)


def stories(request):
    form = UserPostForm()
    data = {"title": "Posts", 'form': form}
    if request.method == "POST":
        new_post = UserPostForm(request.POST)
        if new_post.is_valid():
            name = new_post.cleaned_data['name']
            story = new_post.cleaned_data['post']
            logger.info(f'Add new story from {name}')
            new_post.save()
            new_story_notification(name, story)
            return redirect('/stories_add')
    return render(request, "pages/stories.html", context=data)


def stories_add(request):
    data = {"title": "Stories was add", }
    return render(request, "pages/stories_add.html", context=data)


def help_us(request):
    data = {"title": "Help Us"}
    return render(request, "pages/help-us.html", context=data)


def pageNotFound(request, exception):
    data = {"title": "Ops, something is wrong"}
    return render(request, "pages/error.html", context=data)
