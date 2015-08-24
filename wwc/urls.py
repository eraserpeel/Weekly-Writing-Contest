from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import view_profile

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url('', include('main.urls')),
)
