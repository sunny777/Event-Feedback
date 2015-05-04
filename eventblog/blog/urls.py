__author__ = 'User'

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url( r'^$', 'blog.views.blog', name='blog'),
    url(r'^(?P<id>[0-9]+)/$', views.blog, name='blog'),
)