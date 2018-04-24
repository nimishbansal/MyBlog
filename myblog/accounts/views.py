from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserProfileForm


class SignUp(generic.CreateView):
    # form_class = UserCreationForm
    form_class = UserProfileForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


#are yaha der se load ho raha h