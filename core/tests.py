from django.test import TestCase
from django.urls import reverse


class BaseViewTestCase(TestCase):
    """ Base test-case for views """
    name = None
    template = None

    def test_get(self):
        response = self.client.get(reverse(self.name))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template)

class TestIndexView(BaseViewTestCase):
    """ Testing main view """
    name = 'main'
    template = 'pages/main/main.html'


class TestPostsView(BaseViewTestCase):
    """ Testing posts view """
    name = 'blog'
    template = 'pages/blog/blog.html'


class TestStoriesView(BaseViewTestCase):
    """ Testing stories view """
    name = 'stories'
    template = 'pages/stories/stories.html'
    template_add = 'pages/stories/stories_add.html'

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
        response = self.client.post(reverse(self.name), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_add)

class TestTestView(BaseViewTestCase):
    """ Testing process_alienation_test view """
    name = 'process_alienation_test'
    template = 'pages/test-blocks/test.html'

    # TODO: write test with post request
    def test_post(self):
        pass
