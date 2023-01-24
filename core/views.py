import os
import logging

from django.http import FileResponse
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
    template = "pages/main.html"
    form = UserPostForm()
    data = {"title": "Voices of Hope", "forms": form}
    if request.method == 'POST':
        email = request.POST.get('email')
        signing_up_for_an_online_group_notification(email)
        return render(request, "pages/main.html", context=data)
    return render(request, template, context=data)


def resources(request):
    template = "pages/resources.html"

    # Files
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    documents_list = os.listdir(f'{base_dir}/documents/')

    data = {
        "title": "Resources of Hope",
        'links': Link.objects.all(),
        'documents': documents_list,
    }
    return render(request, template, context=data)


def download_file(request, file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    document_path = f'{base_dir}/documents/{file_name}'
    open_document = open(document_path, 'rb')
    response = FileResponse(open_document, as_attachment=True, filename=file_name)
    return response


def blog(request):
    template = 'pages/blog.html'
    data = {"title": "Posts", "posts": Post.objects.all()}
    return render(request, template, context=data)


def stories(request):
    template = "pages/stories.html"
    form = UserPostForm()

    data = {"title": "Posts", 'form': form}
    if request.method == "POST":
        new_post = UserPostForm(request.POST)
        if new_post.is_valid():
            name = new_post.cleaned_data['name']
            logger.info(f'Add new story from {name}')
            new_post.save()
            new_story_notification(name)
            return redirect('/stories_add')
    return render(request, template, context=data)


def stories_add(request):
    template = "pages/stories_add.html"
    data = {"title": "Stories was add", }
    return render(request, template, context=data)


def pageNotFound(request, exception):
    template = "pages/error.html"
    data = {"title": "Ops, something is wrong"}
    return render(request, template, context=data)
