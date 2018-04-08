from django.conf.urls import url,include
from django.contrib import admin

from .views import my_create_view, CreatePost, AutomationListView
from . import views

urlpatterns = [
    url(r"^$",views.index),
    url(r"aboutme/",views.AboutMe,name="aboutme"),
    # url(r"create/",CreatePost.as_view(),name="create"),
    url(r"automation/", AutomationListView.as_view(), name="automation"),

    url(r"create/", my_create_view, name="create"),

]
