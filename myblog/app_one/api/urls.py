from django.conf.urls import url,include,re_path
from django.contrib import admin
from . import views


urlpatterns =[
    url(r"^$",views.POSTListAPIView.as_view()),
    url(r"^create/$",views.POSTCreateAPIView.as_view())
]
