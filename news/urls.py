from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include 

from . import views
from news.models import Articles

from django.views.generic import ListView, DetailView

urlpatterns = [
    
    url(r'^', views.index),
    url(r'^$', ListView.as_view(queryset=Articles.objects.all(),
    template_name="news/news.html"
    )),
    
]
