# -*- coding: utf-8 -*-
"""URL routing patterns for {{ cookiecutter.repo_name }}."""

from django.conf.urls import patterns, include, url
from django.contrib import admin

from {{ cookiecutter.app_name }}.urls import (
    urlpatterns as {{ cookiecutter.app_name }}_urlpatterns)

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include({{ cookiecutter.app_name }}_urlpatterns)),
)

