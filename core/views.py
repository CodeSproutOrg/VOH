from django.shortcuts import render

from .forms import UserPostForm, OnlineGroupForm, CoParentingForm
from .func import stories_func, calculate_score, make_a_list_of_documents_func, providing_files_for_download_func
from .models import Link

menu = {
    'VOICES OF HOPE': '/stories',
    'BLOG': '/blog',
    'RESOURCES': {
        'Links': '/links',
        'Videos': '/videos',
        'Documents': '/documents',
        'Apps': '/apps',
    }
}

# Template folders
template_path = 'pages'
main_path = f'{template_path}/main'
blog_path = f'{template_path}/blog'
stories_path = f'{template_path}/stories'
resources_path = f'{template_path}/resources-blocks'
pa_test_path = f'{template_path}/test-blocks'
service_path = f'{template_path}/service'
error_path = f'{template_path}/error'


def index(request):
    template = f"{main_path}/main.html"
    form = OnlineGroupForm(request.POST)
    data = {"title": "Voices of Hope", "menu": menu, "forms": form}

    if form.is_valid():
        # main_func(form)
        return render(request, template, context=data)
    else:
        return render(request, template, context=data)

def blog(request, post_slug=None):
    data = {'menu': menu}

    if not post_slug:
        template = f'{blog_path}/blog.html'
        data["title"] = "Posts"
        return render(request, template, context=data)
    else:
        template = f'{blog_path}/post.html'
        data["title"] = f"Post {post_slug}"
        data['post_slug'] = post_slug
        return render(request, template, context=data)

def stories(request):
    template = f'{stories_path}/stories.html'
    template_complete = f'{stories_path}/stories_add.html'

    form = UserPostForm(request.POST)
    data = {"menu": menu, 'form': form}

    if form.is_valid():
        stories_func(form)
        data['title'] = "Stories was add"
        return render(request, template_complete, context=data)
    else:
        data['title'] = "Posts"
        return render(request, template, context=data)

def process_alienation_test(request):
    templates = {
        'get_template': f"{pa_test_path}/test.html",
        'post_template': f"{pa_test_path}/score.html"
    }
    form = CoParentingForm(request.POST)
    data = { "title": "Posts", "menu": menu, 'form': form }

    if form.is_valid():
        context = calculate_score(form)
        return render(request, templates['post_template'], context)
    else:
        return render(request, templates['get_template'], context=data)

def links_view(request):
    template = f"{resources_path}/links.html"
    data = {
        "title": "Resources of Hope",
        "menu": menu,
        'links': Link.objects.all(),
        'links_sections': [
            'Collaborative Divorce Resources', 'Collaborative Co-Parenting Mediation Resources',
            'Assessments and Screeners', 'Consultation and Therapy Services', 'Co-Parenting Mediation Program'
        ]
    }
    return render(request, template, context=data)

def videos_view(request):
    template = f"{resources_path}/videos.html"
    data = {"title": "Resources of Hope", "menu": menu}
    return render(request, template, context=data)

def apps_view(request):
    template = f"{resources_path}/apps.html"
    data = {"title": "Resources of Hope", "menu": menu}
    return render(request, template, context=data)

def documents_view(request):
    """ View for /resources-blocks/documents.html """
    template = f"{resources_path}/documents.html"

    data = {
        "title": "Resources of Hope",
        "menu": menu,
        'documents': make_a_list_of_documents_func()
    }
    return render(request, template, context=data)

def download_file(request, file_name):
    response = providing_files_for_download_func(file_name)
    return response

def developers_view(request):
    template = f"{service_path}/developers.html"
    data = {"title": "For developers", "menu": menu}
    return render(request, template, context=data)

def pageNotFound(request, exception):
    template = f"{error_path}/error.html"
    data = {"title": "Ops, something is wrong", "menu": menu}
    return render(request, template, context=data)
