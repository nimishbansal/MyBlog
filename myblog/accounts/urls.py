from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    url('signup/', views.SignUp.as_view(), name='signup'),
]