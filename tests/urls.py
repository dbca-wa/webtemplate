from django.urls import path

from tests import views

urlpatterns = [
    path("test/", views.TestPage.as_view(), name="test_page"),
    path("test2/", views.TestPage2.as_view(), name="test_page_2"),
    # We need the following named URLs to render the base template.
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
