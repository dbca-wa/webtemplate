# DBCA Django web template

This project consists of a basic Django application containing HTML
templates that provide a starting point for web applications used by the
[Department](http://www.dbca.wa.gov.au). The base template consists of a mobile-friendly
HTML5 template with a fixed top navbar, plus static assets.
The project also contains functional examples of **login** and
**logged out** templates.

The base template is based upon [HTML5 Boilerplate](https://html5boilerplate.com).

## Development

Dependencies for this project are managed using [uv](https://docs.astral.sh/uv/).
With uv installed, change into the project directory and run:

    uv sync

Activate the virtualenv like so:

    source .venv/bin/activate

Manage new or updated project dependencies with uv also, like so:

    uv add newpackage==1.0

Run unit tests using `pytest` (or `tox`, to test against multiple Python versions):

    pytest -sv
    tox -v

## Releases

Tagged releases are built and pushed to PyPI automatically using a GitHub
workflow in the project. Update the project version in `pyproject.toml` and
tag the required commit with the same value to trigger a release. Packages
can also be built and uploaded manually, if desired.

Build the project locally using uv, [publish to the PyPI registry](https://docs.astral.sh/uv/guides/publish/#publishing-your-package)
using the same tool if you require:

    uv build
    uv publish

## Installation

1. Install: `uv add webtemplate-dbca`.
1. Add `'webtemplate_dbca'` to `INSTALLED_APPS`.
1. Ensure that the `staticfiles` application is included and configured
   correctly.
1. (Optional) Ensure that you have defined the following named URLs: `login` and
   `logout` (this requirement can be overriden, see below).
1. Extend the included base template by placing the following at the head
   of your own templates, e.g. `{% extends "webtemplate_dbca/base.html" %}`
1. Place page content within the required blocks (see below).

## Included CSS and JavaScript

The base template includes the following CSS and JavaScript assets:

- Modernizr (HTML5 polyfills)
- Bootstrap 5 (CSS & JS)

Additional styling can be included using the `extra_style` or `extra_js`
blocks, like so::

    {% load static from staticfiles %}

    {% block extra_style %}
    {{ block.super }}
    <link rel="stylesheet" href="{% static 'css/custom.css' %}">
    {% endblock %}

You can also overide the `base_style` and `base_js` blocks completely to
use different CSS or JS libraries. Note that you will also need to replace the
`top_navbar` block contents if you replace the base Bootstrap CSS & JS.

## Template blocks

The base template contains a number of block tags that are used to render the
content of your project. The main template content blocks are as follows:

- `navbar_links` - used to define navigation links in the top navbar.
- `navbar_auth` - used to display either a **Login** or **Logout** link.
- `page_content` - used to contain the page's main content.
- `page_footer` - used to contain a page footer area.

Note that the `navbar_auth` block contains `{% url %}` templatetags with
named URLs called _login_ and _logout_. If this is not required or
inappropriate for your project, simply override the `navbar_auth` block
in the base template like so::

    {% block navbar_auth %}{% endblock %}

In addition, a number of context variables are defined:

- `page_title` - used to populate the page **<title>** tags.
- `site_title` - used to populate the projects's title in the top navbar.
- `site_acronym` - used to populate a shorter title in the navbar (B4 template).

Context variables should be passed to templates in every view.

## Bootstrap 5 examples

To extend the base template with an optional row to display alert messages plus
a shaded footer div, try the following (further page content is then injected to
the `page_content_inner` block)::

    {% extends "webtemplate_dbca/base.html" %}

    {% block extra_style %}
    <style>
        .footer {background-color: lightgrey}
    </style>
    {% endblock %}

    {% block page_content %}
        <div class="container-fluid">
            <!-- Messages  -->
            {% if messages %}
            <div class="row">
                <div class="col">
                    {% for message in messages %}
                    <div class="alert{% if message.tags %} alert-{{ message.tags }}{% endif %}">
                        {{ message|safe }}
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endif %}

            <div class="row">
                <div class="col">
                    {% block page_content_inner %}{% endblock %}
                </div>
            </div>
        </div>
    {% endblock %}

    {% block page_footer %}
    <footer class="footer mt-auto py-3">
        <div class="container-fluid">
            <div class="row">
                <div class="col">
                    <small class="float-right">&copy; Department of Biodiversity, Conservation and Attractions</small>
                </div>
            </div>
        </div>
    </footer>
    {% endblock page_footer %}
