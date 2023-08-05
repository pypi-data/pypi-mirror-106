# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['titofisto']

package_data = \
{'': ['*']}

install_requires = \
['Django>2.2,<4.0']

setup_kwargs = {
    'name': 'django-titofisto',
    'version': '0.1.0',
    'description': 'Django Time-Token File Storage',
    'long_description': 'Django Time-Token File Storage\n==============================\n\nThis is a simple extension to Django\'s `FileSystemStorage` that adds a URL\nparameter carrying a shared token, which is only valid for a defined period\nof time.\n\nFunctionality\n-------------\n\nThis is a drop-in replacement for the Django `FileSystemStorage`, usable if\nmedia files are served by Django itself. It does currently not work if media\nfiles are served from an independent web server.\n\nThe storage and its accompanying view do the following:\n\n* When a URL to a storage file is generated, a HMAC-based token is generated\n* The token and the timestamp when it was generated are appended as request\n  parameters to the URL\n* Upon retrieval of the file through the accompanying view, the requested\n  file name and the passed timestamp are used to recalculate the HMAC-based\n  token\n* Only if the tokens match, and a configured timeout has not passed, is the\n  file served\n\nThe HMAC-based token ensures that the token is invalidated when:\n\n* The filename changes\n* The timestamp changes\n* The mtime of the file changes\n* The `SECRET_KEY` changes\n\nThe HMAC is salted with the `SECRET_KEY`.\n\nInstallation\n------------\n\nTo add `django-titofisto`_ to a project, first add it as dependency to your\nproject, e.g. using `poetry`_::\n\n  $ poetry add django-titofisto\n\n`django-titofisto` will use the base `FileSystemStorage` for almost everything,\nincluding determining the `MEDIA_ROOT`. It merely adds a token as URL parameter\nto whatever the base `FileSystemStorage.url()` method returns.\n\nAdd the following to your settings::\n\n  DEFAULT_FILE_STORAGE = "titofisto.TitofistoStorage"\n  TITOFISTO_TIMEOUT = 3600  # optional, this is the default\n  TITOFISTO_PARAM_PREFIX = "titofisto_"  # optional, this is the default\n\nAdd the following to your URL config::\n\n  from django.conf import settings\n  from django.urls import include, path\n\n  urlpatterns += [\n      path(settings.MEDIA_URL, include("titofisto.urls")),\n  ]\n\nDjango will start serving media files under the configured `MEDIA_URL`.\n\n.. _django-titofisto: https://edugit.org/AlekSIS/libs/django-titofisto\n.. _poetry: https://python-poetry.org/\n.. _Django\'s cache framework: https://docs.djangoproject.com/en/3.2/topics/cache/\n',
    'author': 'Dominik George',
    'author_email': 'dominik.george@teckids.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://edugit.org/AlekSIS/libs/django-titofisto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
