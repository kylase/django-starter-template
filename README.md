# Django Starter Template

![Django CI](https://github.com/kylase/django-starter-template/actions/workflows/django.yml/badge.svg)

This is a simple template for quick kickstart of Django projects. The dependencies required in this template are:
1. `pytest`, `pytest-django`, `pytest-cov` for testing
1. `django-extensions` and `ipython` for enhanced shell
1. `django-debug-toolbar`for debugging

# Quick Start (Development)

1. Clone the project using `git clone`.
1. Rename the top-level `django-starter-template` if you have not clone it as `<YourProject>` and directory `project` to your project name `<YourProject>`
  1. In `settings.py`, change the value of `ROOT_URLCONF` to `<YourProject>.urls`
  1. In `settings.py`, change the value of `WSGI_APPLICATION` to `<YourProject>.wsgi.application`
1. Create an environment variable named `SECRET_KEY`
1. Create an environment variable named `ENV` to `dev` if for development purpose
1. In `pytest.ini`, change `DJANGO_SETTINGS_MODULE` to `<YourProject>.settings`. Optionally, you can set `DJANGO_SETTINGS_MODULE` as an environment variable that points to your `settings` e.g. `<YourProject>.settings`.
1. Rename `CustomUser` in `common/models.py` to `<YourUserClass>` as this is the [recommended](https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project) way to extend the default `User` class in the future.
1. Run `pip install -r requirements/dev.txt` to install third-party dependencies

# Guide

- `requirements/dev.txt` is for development packages
- `requirements/test.txt` is for testing packages
- `requirements/prod.txt` is for production packages
