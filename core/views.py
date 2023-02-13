import logging
import os

from django.http import FileResponse
from django.shortcuts import render

from .forms import UserPostForm
from .mail_notification import new_story_notification, signing_up_for_an_online_group_notification
from .models import Post, Link

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

def blog(request):
    template = 'pages/blog.html'
    data = {"title": "Posts", "posts": Post.objects.all()}
    return render(request, template, context=data)

def stories(request):
    template_folder = 'pages/stories'
    template = f'{template_folder}/stories.html'
    redirect_template = f'{template_folder}/stories_add.html'

    form = UserPostForm()

    if request.method != "POST":
        data = {"title": "Posts", 'form': form}
        return render(request, template, context=data)
    else:
        data = {"title": "Stories was add", }
        new_post = UserPostForm(request.POST)
        if new_post.is_valid():
            name = new_post.cleaned_data['name']
            logger.info(f'Add new story from {name}')
            new_post.save()
            new_story_notification(name)

            return render(request, redirect_template, context=data)

def process_alienation_test(request):
    get_template = 'pages/test-blocks/test.html'
    post_template = 'pages/test-blocks/score.html'
    if request.method != 'POST':
        return render(request, get_template)
    else:
        answers = list()
        for question in range(1, 11):
            answer = int(request.POST.get(f'question{question}'))
            answers.append(answer)

        score = sum(answers)

        if score <= 2:
            results = 'Low likelihood of parental alienation'
        elif score <= 4:
            results = 'Moderate likelihood of parental alienation'
        else:
            results = 'High likelihood of parental alienation'

        # Render the results page with the calculated score and results
        return render(request, post_template, {'score': score, 'results': results})

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
