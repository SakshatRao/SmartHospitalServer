from django.contrib import admin
from django.conf.urls import include
from django.urls import re_path
from . import views

app_name = 'patient'

urlpatterns = [
    re_path(r'^$', views.homepage_view, name = 'homepage'),
    re_path(r'^health_status/$', views.health_status_view, name = 'health-status'),
    re_path(r'^temperature_graph/$', views.temperature_graph_view, name = 'temperature_graph'),
    re_path(r'^spO2_graph/$', views.spO2_graph_view, name = 'spO2_graph'),
    re_path(r'^bpm_graph/$', views.bpm_graph_view, name = 'bpm_graph'),
]