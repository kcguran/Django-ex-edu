import imp
from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("blogs/<int:id>", views.blogDetails, name="blog_details"),

]
