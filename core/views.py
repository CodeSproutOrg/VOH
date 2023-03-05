import os

from django.http import FileResponse
from django.shortcuts import render

from .forms import UserPostForm, OnlineGroupForm, CoParentingForm
from .func import main_func, stories_func, calculate_score
from .models import Post, Link

template_path = 'pages'

def index(request):
    template = f"{template_path}/main.html"
    form = OnlineGroupForm(request.POST)
    data = {"title": "Voices of Hope", "forms": form}
    if form.is_valid():
        main_func(form)
        return render(request, template, context=data)
    else:
        return render(request, template, context=data)

def blog(request, post_id=None):
    template = f"{template_path}/blog"

    if not post_id:
        template = f'{template}/blog.html'
        data = {"title": "Posts", "posts": Post.objects.all()}
        return render(request, template, context=data)
    else:
        template = f'{template}/post.html'
        post = Post.objects.get(id=post_id)
        data = {"title": post.title, "post": post}
        return render(request, template, context=data)

def stories(request):
    template_folder = f"{template_path}/stories"
    template = f'{template_folder}/stories.html'
    redirect_template = f'{template_folder}/stories_add.html'

    form = UserPostForm(request.POST)
    data = {"title": None, 'form': form}

    if form.is_valid():
        stories_func(form)
        data['title'] = "Stories was add"
        return render(request, redirect_template, context=data)
    else:
        data['title'] = "Posts"
        return render(request, template, context=data)

def process_alienation_test(request):
    template_path_test = f'{template_path}/test-blocks'
    templates = {
        'get_template': f"{template_path_test}/test.html",
        'post_template': f"{template_path_test}/score.html"
    }
    form = CoParentingForm(request.POST)
    data = {'form': form}

    if form.is_valid():
        context = calculate_score(form)
        return render(request, templates['post_template'], context)
    else:
        return render(request, templates['get_template'], context=data)

def resources(request):
    template = f"{template_path}/resources.html"

    # Files
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    documents_list = os.listdir(f'{base_dir}/documents/')

    data = {
        "title": "Resources of Hope",
        'links': Link.objects.all(),
        'links_sections': [
            'Collaborative Divorce Resources', 'Collaborative Co-Parenting Mediation Resources',
            'Assessments and Screeners', 'Consultation and Therapy Services', 'Co-Parenting Mediation Program'
        ],
        'documents': documents_list
    }
    return render(request, template, context=data)

def download_file(request, file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    document_path = f'{base_dir}/documents/{file_name}'
    open_document = open(document_path, 'rb')
    response = FileResponse(open_document, as_attachment=True, filename=file_name)
    return response

def pageNotFound(request, exception):
    template = "pages/error.html"
    data = {"title": "Ops, something is wrong"}
    return render(request, template, context=data)
