import logging
import os

from django.core.mail import send_mail
from django.http import FileResponse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(funcName)s - %(message)s",
    handlers=[logging.FileHandler('./server.log', encoding='utf-8')]
)
logger = logging.getLogger(__name__)

def stories_func(form):
    form.save()
    name = form.cleaned_data['name']
    new_story_notification(name)
    logger.info(f'Add new story from {name}')

def calculate_score(form):
    answers = [int(form.cleaned_data[f'question{question}']) for question in range(1, 11)]
    score = sum(answers)
    results = (
        'Low likelihood of parental alienation' if score <= 2 else
        'Moderate likelihood of parental alienation' if score <= 4 else
        'High likelihood of parental alienation'
    )
    context = {'score': score, 'results': results}
    return context

def new_story_notification(name: str) -> str:
    send_mail('New voices was sent',
              f'New Voices of Hope was added by {name}',
              'empowermentonlline@gmail.com',
              ['empowermentonlline@gmail.com', ]
              )
    return 'New story -200'

def make_a_list_of_documents_func():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    documents_list = os.listdir(f'{base_dir}/static/documents/')
    return documents_list

def providing_files_for_download_func(file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    document_path = f'{base_dir}/static/documents/{file_name}'
    open_document = open(document_path, 'rb')
    response = FileResponse(open_document, as_attachment=True, filename=file_name)
    return response


# These functions aren't using but in future will be
#
# def main_func(form):
#     # email = form.data['email']
#     # signing_up_for_an_online_group_notification(email)
# def signing_up_for_an_online_group_notification(email: str) -> str:
#     if email != '':
#         send_mail('Signing up for an online group',
#                   email,
#                   'empowermentonlline@gmail.com',
#                   ['empowermentonlline@gmail.com', ]
#                   )
#     return 'New entry to the online group -200'
