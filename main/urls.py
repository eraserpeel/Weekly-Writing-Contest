from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import home
from main.views import view_profile

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^view_profile/', view_profile, name='view_profile'),
    
]
