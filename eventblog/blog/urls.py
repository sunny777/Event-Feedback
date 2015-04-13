__author__ = 'User'

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url( r'^$', 'blog.views.blog', name='blog'),
    #url( r'^$', 'blog.views.blog_save', name='blog_save'),
)