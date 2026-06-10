from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.test.client import Client
from django.urls import reverse


class BaseTemplateTest(TestCase):
    client = Client()

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        # Create a throwaway user object.
        self.user = User.objects.create_user(
            username="john", email="john@email.com", password="secret"
        )

    def tearDown(self):
        # Delete the user after each test case.
        self.user.delete()

    def test_base_template_render(self):
        """Test that the base template renders with expected content."""
        url = reverse("test_page")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "webtemplate_dbca/base.html")
        self.assertContains(
            response, '<a class="nav-link" id="id_a_login" href="/login/">Log in</a>'
        )
        self.assertContains(response, "<title>Test Bootstrap 5 page</title>")

    def test_page_2_template_render(self):
        """Test that the page 2 view renders with expected content."""
        url = reverse("test_page_2")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "webtemplate_dbca/base.html")
        self.assertContains(response, "Hello, World!")
