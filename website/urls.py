from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^getStationById/([0-9]+)', getStationById),
    url(r'^$', index)
]
