__author__ = 'User'

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    #url(r'^$', views.DashboardView.as_view(template_name='dashboard.html')),
    url( r'^$', 'dashboard.views.dashboard', name='dashboard'),
    # url(r'^(?P<event_id>\d+)/$', views.BlogView.detail, name='detail'),
)