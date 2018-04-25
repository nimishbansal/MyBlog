from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from app_one.models import User
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



#are yaha der se load ho raha h