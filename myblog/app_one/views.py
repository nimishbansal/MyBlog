# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from functools import partial
from django import forms
from django.forms import BaseForm

from django.forms.utils import ErrorList
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, ListView, CreateView

from .forms import CommentModelForm,CreateForm
from .models import Post, Comment


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





#
#
#
# class CreatePost(CreateView):
#     # queryset = Post.objects.all()
#     model = Post
#     fields = ["title","code_text"]
#     template_name = "app_one/createPost.html"
#     success_url = "/app_one/create"
#     http_method_names = ["get","post"]
#
#     def get_context_data(self, **kwargs):
#         context=super(CreatePost,self).get_context_data(**kwargs)
#         print(self.request.method)
#         # context["alert"]=1
#         # context["post_title"]="hello"
#         return context
#
#



class CreatePost(FormView):
    form_class = CreateForm
    template_name = "app_one/createPost.html"
    model = Post
    success_url = "app_one/create"



class AutomationListView(ListView):
    queryset = Post.objects.filter(post_type="automation")
    context_object_name = "blogobject"
    template_name = "app_one/automation.html"


class AndroidListView(ListView):
    queryset = Post.objects.filter(post_type="android")
    context_object_name = "blogobject"
    template_name = "app_one/android.html"


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = "app_one/post_detail.html"
    context_object_name = "object"
    def get_object(self):
        pk = self.kwargs.get('pk')
        object = get_object_or_404(Post, post_id=pk)
        return object

    def get_context_data(self, **kwargs):
        context=super(PostDetailView, self).get_context_data(**kwargs)
        context["commentCreateForm"]=CommentModelForm()
        return context


class PostDetailCommentCreateView(CreateView):
    model=Comment
    template_name = "app_one/post_detail.html"
    fields = ["comment_text"]

    def get_success_url(self, *args,**kwargs):
        print("getting success url")
        print(*args)
        print(**kwargs)
        # obj = form.instance or self.object
        url=reverse_lazy("detail", kwargs={'pk': self.kwargs["pk"]})
        print(url)
        return url

    def get_object(self):
        pk = self.kwargs.get('pk')
        print(pk)
        object = get_object_or_404(Post, post_id=pk)
        return object


    def as_p(self,form):
        "Return this form rendered as HTML <p>s."
        return form._html_output(
            normal_row='<p%(html_class_attr)s>%(label)s %(field)s%(help_text)s</p>',
            error_row='<b> %s </b>',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)

    def form_valid(self, form:BaseForm):


        obj = form.save(commit=False)
        obj.post_id=get_object_or_404(Post, post_id=self.kwargs.get('pk'))

        try:
            obj.user = self.request.user
            obj.save()
        except Exception as E:
            print(E)
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["user must be logged in to continue"])
            return super(PostDetailCommentCreateView, self).form_invalid(form)


        return HttpResponseRedirect(self.get_success_url())


    def get_context_data(self, **kwargs):
        context=super(PostDetailCommentCreateView, self).get_context_data(**kwargs)
        context["form"]["comment_text"].label=""
        context["form"].as_p=partial(self.as_p,context["form"])
        context["success_url"]=reverse_lazy("detail", kwargs={'pk': self.kwargs["pk"]})

        print(context)
        context["object"]=self.get_object()
        return context







