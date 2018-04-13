from django.conf.urls import url,include,re_path
from django.contrib import admin


from .views import my_create_view, CreatePost, AutomationListView, AndroidListView, AutomationDetailView
from . import views

urlpatterns = [
    url(r"^$",views.index),
    url(r"aboutme/",views.AboutMe,name="aboutme"),
    # url(r"create/",CreatePost.as_view(),name="create"),
    url(r"automation/", AutomationListView.as_view(), name="automation_list"),
    url(r"android/", AndroidListView.as_view(), name="android_list"),
    url(r"create/", my_create_view, name="create"),
    url(r"posts/(?P<pk>\d+)/$",AutomationDetailView.as_view())

]
