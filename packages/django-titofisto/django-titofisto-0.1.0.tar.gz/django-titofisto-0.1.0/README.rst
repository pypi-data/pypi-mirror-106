Django Time-Token File Storage
==============================

This is a simple extension to Django's `FileSystemStorage` that adds a URL
parameter carrying a shared token, which is only valid for a defined period
of time.

Functionality
-------------

This is a drop-in replacement for the Django `FileSystemStorage`, usable if
media files are served by Django itself. It does currently not work if media
files are served from an independent web server.

The storage and its accompanying view do the following:

* When a URL to a storage file is generated, a HMAC-based token is generated
* The token and the timestamp when it was generated are appended as request
  parameters to the URL
* Upon retrieval of the file through the accompanying view, the requested
  file name and the passed timestamp are used to recalculate the HMAC-based
  token
* Only if the tokens match, and a configured timeout has not passed, is the
  file served

The HMAC-based token ensures that the token is invalidated when:

* The filename changes
* The timestamp changes
* The mtime of the file changes
* The `SECRET_KEY` changes

The HMAC is salted with the `SECRET_KEY`.

Installation
------------

To add `django-titofisto`_ to a project, first add it as dependency to your
project, e.g. using `poetry`_::

  $ poetry add django-titofisto

`django-titofisto` will use the base `FileSystemStorage` for almost everything,
including determining the `MEDIA_ROOT`. It merely adds a token as URL parameter
to whatever the base `FileSystemStorage.url()` method returns.

Add the following to your settings::

  DEFAULT_FILE_STORAGE = "titofisto.TitofistoStorage"
  TITOFISTO_TIMEOUT = 3600  # optional, this is the default
  TITOFISTO_PARAM_PREFIX = "titofisto_"  # optional, this is the default

Add the following to your URL config::

  from django.conf import settings
  from django.urls import include, path

  urlpatterns += [
      path(settings.MEDIA_URL, include("titofisto.urls")),
  ]

Django will start serving media files under the configured `MEDIA_URL`.

.. _django-titofisto: https://edugit.org/AlekSIS/libs/django-titofisto
.. _poetry: https://python-poetry.org/
.. _Django's cache framework: https://docs.djangoproject.com/en/3.2/topics/cache/
