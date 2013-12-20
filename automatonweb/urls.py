from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'automatonweb.views.home', name='home'),
    url(r'^dot-graph/', 'automatonweb.views.dot_graph'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
