from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = "webtemplate_dbca/base.html"

    def get_context_data(self, **kwargs):
        context = super(TestPage, self).get_context_data(**kwargs)
        context["page_title"] = "Test page"
        context["page_description"] = "Meta tag page description"
        context["site_title"] = "SITE TITLE"
        return context


class TestDBCAPage(TemplateView):
    template_name = "webtemplate_dbca/base_dbca.html"

    def get_context_data(self, **kwargs):
        context = super(TestDBCAPage, self).get_context_data(**kwargs)
        context["page_title"] = "Test page"
        context["page_description"] = "Meta tag page description"
        context["site_title"] = "SITE TITLE"
        return context


class TestPage2(TestPage):
    template_name = "tests/test_page2.html"


class TestInternetPage(TemplateView):
    template_name = "webtemplate_dbca/base_internet.html"

    def get_context_data(self, **kwargs):
        context = super(TestInternetPage, self).get_context_data(**kwargs)
        context["page_title"] = "Test page"
        context["page_description"] = "Meta tag page description"
        context["site_title"] = "SITE TITLE"
        return context


class TestB4Page(TemplateView):
    template_name = "webtemplate_dbca/base_b4.html"

    def get_context_data(self, **kwargs):
        context = super(TestB4Page, self).get_context_data(**kwargs)
        context["page_title"] = "Test page"
        context["page_description"] = "Meta tag page description"
        context["site_title"] = "SITE TITLE"
        return context


class TestB5Page(TemplateView):
    template_name = "webtemplate_dbca/base_b5.html"

    def get_context_data(self, **kwargs):
        context = super(TestB5Page, self).get_context_data(**kwargs)
        context["page_title"] = "Test Bootstrap 5 page"
        context["page_description"] = "Meta tag page description"
        context["site_title"] = "SITE TITLE"
        return context
