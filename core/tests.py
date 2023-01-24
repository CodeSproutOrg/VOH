from django.test import TestCase
from django.urls import reverse

from core.models import UserPost


class TestIndexView(TestCase):
    """ Testing main view """

    def test_get(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/main.html')


class TestLibraryView(TestCase):
    """ Testing resources view """

    def test_get(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/resources.html')


class TestPostsView(TestCase):
    """ Testing posts view """

    def test_get(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/blog.html')


class TestStoriesView(TestCase):
    """ Testing stories view """

    def test_get(self):
        response = self.client.get(reverse('stories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/stories.html')


    def test_post(self):
        data = {
            'name': 'John Doe',
            'case': 'Test case',
            'abuse_from_CPS_DCFS': 'Substantiated',
            'parental_alienation': 'Mild',
            'allegations': 'Yes',
            'falsified': 'No',
            'duration': 'Test duration',
            'money': 'Test money',
            'left_broken': 'Test left broken',
            'abuse_criteria': 'Test abuse criteria',
            'result': 'Test result'
        }
        response = self.client.post(reverse('stories'), data=data)
        self.assertEqual(UserPost.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
