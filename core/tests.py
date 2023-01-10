from django.test import TestCase
from django.urls import reverse

from core.models import UserPost


class TestIndexView(TestCase):
    """ Testing main view """
    def test_get(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/main.html')


class TestLinksView(TestCase):
    """ Testing links view """
    def test_get(self):
        response = self.client.get(reverse('links'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/links.html')


class TestPostsView(TestCase):
    """ Testing posts view """
    def test_get(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/posts.html')


class TestStoriesView(TestCase):
    """ Testing stories view """
    def test_get(self):
        response = self.client.get(reverse('stories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/stories.html')

    def test_post(self):
        """ Testing POST method """
        data = {'name': 'Test User', 'post': 'Test post'}
        response = self.client.post(reverse('stories'), data=data)

        user_post = UserPost.objects.get(name=data['name'])
        self.assertEqual(user_post.name, data['name'])
        self.assertEqual(response.status_code, 302)


class TestHelpUsView(TestCase):
    """ Testing links view """
    def test_get(self):
        response = self.client.get(reverse('help-us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/help-us.html')
