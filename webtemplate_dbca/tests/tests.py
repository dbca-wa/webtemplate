from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.test.client import Client
from django.urls import reverse


class BaseTemplateTest(TestCase):
    client = Client()

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        # Create a throwaway user object.
        self.user = User.objects.create_user(
            username='john', email='john@email.com', password='secret')

    def tearDown(self):
        # Delete the user after each test case.
        self.user.delete()

    def test_base_template_render(self):
        """Test that the base template renders with expected content.
        """
        url = reverse('test_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webtemplate_dbca/base.html')
        self.assertContains(response, '<a id="id_a_login" href="/login/">Log in</a>')
        self.assertNotContains(response, 'Log out')  # No 'log out' text.
        self.assertContains(response, '<title>Test page</title>')
        self.assertContains(response, '<a class="navbar-brand" href="/">SITE TITLE</a>')
        self.assertContains(response, '<li class="active"><a href="#">Link 1</a></li>')

    def test_base_dbca_template_render(self):
        """Test that the base_dbca template renders with expected content.
        """
        url = reverse('test_dbca_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webtemplate_dbca/base_dbca.html')
        self.assertContains(response, '<a id="id_a_login" href="/login/">Log in</a>')
        self.assertNotContains(response, 'Log out')  # No 'log out' text.
        self.assertContains(response, '<title>Test page</title>')
        self.assertContains(response, '<a class="navbar-brand" href="/">SITE TITLE</a>')
        self.assertContains(response, '<li class="active"><a href="#">Link 1</a></li>')

    def test_base_template_logged_in(self):
        """Test the base template displays a 'Log out' link for logged-in users.
        """
        url = reverse('test_page')
        self.client.login(username='john', password='secret')
        self.assertIn('_auth_user_id', self.client.session)
        response = self.client.get(url)
        self.assertContains(response, '<a id="id_a_logout" href="/logout/">Log out</a>')
        self.assertNotContains(response, 'Log in')  # No 'log in' text.

    def test_base_template_extend(self):
        """Test that the base template renders, with some content overridden.
        """
        url = reverse('test_page_2')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1 id="id_hello_world">Hello, World!</h1>')

    def test_internet_template_render(self):
        """Test that the base_internet template renders with expected content.
        """
        url = reverse('test_internet_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webtemplate_dbca/base_internet.html')
        self.assertContains(response, '<a id="id_a_login" href="/login/">Log in</a>')
        self.assertNotContains(response, 'Log out')  # No 'log out' text.

    def test_base_b4_template_render(self):
        """Test that the base_b4 template renders with expected content.
        """
        url = reverse('test_page_b4')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webtemplate_dbca/base_b4.html')
        self.assertContains(response, '<a class="nav-link" id="id_a_login" href="/login/">Log in</a>')
        self.assertContains(response, '<title>Test page</title>')

    def test_base_b5_template_render(self):
        """Test that the base_b5 template renders with expected content.
        """
        url = reverse('test_page_b5')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webtemplate_dbca/base_b5.html')
        self.assertContains(response, '<a class="nav-link" id="id_a_login" href="/login/">Log in</a>')
        self.assertContains(response, '<title>Test Bootstrap 5 page</title>')
