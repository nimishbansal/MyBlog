from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django import forms
#password include kyo na kar rah bina include kre aarha h to tujhe kya chahiye dikhaata hu
from .models import User


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields=["username","email","password"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude=['user']

