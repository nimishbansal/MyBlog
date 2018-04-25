# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("detail",request.user.username)
    return render(request,"myblog/home.html")
