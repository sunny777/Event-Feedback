__author__ = 'User'

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    #url(r'^$', views.EventView.as_view(template_name='events.html')),
    url(r'^$', 'event.views.event', name='event'),
    url(r'^(?P<id>[0-9]+)/$', views.event, name='event'),
)
