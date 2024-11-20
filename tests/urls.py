from django.urls import path

from .views import (
    TestB4Page,
    TestB5Page,
    TestDBCAPage,
    TestInternetPage,
    TestPage,
    TestPage2,
)

urlpatterns = [
    path("test/", TestPage.as_view(), name="test_page"),
    path("test-dbca/", TestDBCAPage.as_view(), name="test_dbca_page"),
    path("test2/", TestPage2.as_view(), name="test_page_2"),
    path("test-internet/", TestInternetPage.as_view(), name="test_internet_page"),
    path("test-b4/", TestB4Page.as_view(), name="test_page_b4"),
    path("test-b5/", TestB5Page.as_view(), name="test_page_b5"),
    # We need the following named URLs to render the base template.
    path("login/", TestPage.as_view(), name="login"),
    path("logout/", TestPage.as_view(), name="logout"),
]
