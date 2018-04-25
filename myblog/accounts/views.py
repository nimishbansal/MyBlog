from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Email
from app_one.models import User
from myblog import settings
from .forms import UserProfileForm, UserForm


class SignUp(generic.View):


    def get(self, request, *args, **kwargs):
        print("get")
        context_data=self.get_context_data()
        return render(request,"signup.html",context_data)


    def post(self, request, *args, **kwargs):

        user_form=UserForm(request.POST)
        profile_form=UserProfileForm(data=request.POST,files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save(commit=False)
            user.set_password(request.POST["password"])
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            if "photu" in request.FILES:
                profile.photu=request.FILES["photu"]
                print("profile photo is ",request.FILES["photu"])
            profile.save()

            return redirect("login")










    def get_context_data(self):
        context_data={}
        context_data["userform"]=UserForm
        context_data["profileform"]=UserProfileForm
        print(context_data)
        return context_data




    # class SignUp(generic.View):
#     form_class = UserCreationForm
#     # form_class = UserProfileForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


class UserDetailView(generic.DetailView):
    template_name = "accounts/userdetail.html"

    def get_object(self):
        object=get_object_or_404(User,username__iexact=self.kwargs.get("username"))
        print(object.User.following)
        return object

    def get_context_data(self, **kwargs):
        context=super(UserDetailView, self).get_context_data(**kwargs)
        context["MEDIA_URL"]=settings.MEDIA_URL
        return context


class UserFollowView(generic.View):
    """
     FLOW:
     current-user->authenticated->user_to_follow_exists->both are not same->if alreading followingremove else follow
     """
    def get(self,request,username):
        if request.user.is_authenticated:
            user_to_follow=User.objects.filter(username__iexact=username)
            if user_to_follow.count()==1:
                user_to_follow=user_to_follow.get(username=username)
                currentuser=request.user
                if user_to_follow!=currentuser:
                    print(user_to_follow)
                    print(currentuser)
                    currentuserProfile=currentuser.User
                    if user_to_follow in currentuserProfile.following.all():
                        currentuserProfile.following.remove(user_to_follow)
                    else:
                        currentuserProfile.following.add(user_to_follow)

        return redirect("detail",self.kwargs.get("username"))


class EmailView(generic.ListView):
    template_name = "accounts/emails.html"
    # model = Email
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Email.objects.filter(email_receiver=self.request.user)
        else:
            return super(EmailView, self).get_queryset()
    
    def get_context_data(self, *args, **kwargs):
        context=super(EmailView, self).get_context_data(*args,**kwargs)
        if self.request.user.is_authenticated:
            context["email_list"]=Email.objects.filter(email_receiver=self.request.user)
        return context