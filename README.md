# Django Starter Template

This is a simple template for quick kickstart of Django projects. The dependencies required in this template are:
1. `pytest`, `pytest-django`, `pytest-cov` for testing
1. `django-extensions` and `ipython` for enhanced shell
1. `django-debug-toolbar`for debugging

# Quick Start (Development)

1. Rename the top-level `django-starter-template` or what you have clone as and directory `project` to your project name `<your_project>`
  1. In `settings.py`, change the value of `ROOT_URLCONF` to `<your_project>.urls`
  1. In `settings.py`, change the value of `WSGI_APPLICATION` to `<your_project>.wsgi.application`
1. Create an environment variable named `SECRET_KEY`
1. Create an environment variable named `ENV` to `dev` if for development purpose
1. In `pytest.ini`, change `DJANGO_SETTINGS_MODULE` to `<your_project>.settings`. Optionally, you can set `DJANGO_SETTINGS_MODULE` as an environment variable that points to your `settings` e.g. `<your_project>.settings`.
1. Run `pip install -r requirements/dev.txt` to install third-party dependencies

# Guide

- `requirements/dev.txt` is for development packages
- `requirements/test.txt` is for testing packages
- `requirements/prod.txt` is for production packages
