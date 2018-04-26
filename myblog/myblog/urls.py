"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import allauth
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from accounts.views import UserDetailView,UserFollowView,EmailView
from myblog import settings
from . import views

urlpatterns = [
    url(r'^$', views.index,name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^app_one/',include("app_one.urls")),
    url(r'accounts/', include('accounts.urls')),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profiles/(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
    url(r'^profiles/(?P<username>[\w.@+-]+)/mail/$', login_required(EmailView.as_view()), name='mail'),
    url(r'^profiles/(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from allauth import account
from django.contrib.auth.urls import views