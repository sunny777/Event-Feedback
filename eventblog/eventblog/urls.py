from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView
# from blog.views import BlogView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # (r'^blog/$', BlogView.as_view(template_name='blog.html')),
    (r'^blogs/$', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/$', include('event.urls')),
    url(r'^', include('dashboard.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    # (r'^event/$', TemplateView.as_view(template_name='event.html')),
    (r'^account/login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^account/logout$', 'django.contrib.auth.views.logout', {'next_page': '/account/login'}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
