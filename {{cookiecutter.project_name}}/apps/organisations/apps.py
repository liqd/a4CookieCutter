from django.apps import AppConfig


class Config(AppConfig):
    name = 'apps.organisations'
    label = '{{ cookiecutter.project_name }}_organisations'
