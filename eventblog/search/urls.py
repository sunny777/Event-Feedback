__author__ = 'User'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url( r'^$', 'search.views.search', name='search'),

    )