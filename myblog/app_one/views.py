# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render,HttpResponseRedirect,HttpResponse

# Create your views here.
from django.views.generic import CreateView, DetailView

from .forms import CreateForm
from .models import Post


def index(request):
    return render(request,"app_one/home.html")


def AboutMe(request):
    return render(request,"app_one/aboutme.html")


#tu kuch na kar abhi
#
# def check(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse(Post.objects.all()['title'])
#
#         else:
#             print(form.errors)
#
#     else:
#         form =PostForm()
#     return render(request,"app_one/createPost.html",{'form':form})


#mat kar else me mat daal
#
# def custom(request):
#     if request.method == "POST":
#
#         title = request.POST.get("title")
#         code_text = request.POST.get("text_code")
#         Post.title = title
#         Post.code_text = code_text
#         Post.save()
#         return H
#     # bina object ka try karta hu k

#
# def my_create_view(request):#WSGIRequest):
#     print("request method is ",request.method)
#     if request.method=="GET":
#         form = CreateForm()
#         return render(request,"app_one/createPost.html",{"form":form})
#     elif request.method=="POST":
#         form = CreateForm(request.POST)
#         print(form.is_valid())
#         print(form.errors)
#         if (form.is_valid()):
#             print(request.user.is_authenticated)
#             myPostObject=Post(title=form.cleaned_data.get("title"),code_text=form.cleaned_data.get("code_text"))
#             myPostObject.save()
#             form = CreateForm()
#             return render(request, "app_one/createPost.html", {"form": form})
#
#         else:
#             raise forms.ValidationError(form._errors)

def my_create_view(request):
    form=CreateForm(request.POST or None)
    context={
        "form": form
    }
    if form.is_valid():
        print("form is valid")
        instance=form.save(commit=False)
        instance.save()
        context={
            "form":CreateForm(),
            "alert":1,
            "post_title":form.cleaned_data.get("title")
        }
    return render(request,"app_one/createPost.html",context)








# class CreatePost(CreateView):
#     # queryset = Post.objects.all()
#     model = Post
#     fields = ["title","code_text"]
#     template_name = "app_one/createPost.html"
#     success_url = "app_one/create"
