
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include 

from django.views.generic import ListView, DetailView

from . import views


urlpatterns = [
    
    url(r'^', views.index),
    
]
