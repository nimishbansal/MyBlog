from django.contrib.auth.forms import UserCreationForm
from django import forms
#password include kyo na kar rah bina include kre aarha h to tujhe kya chahiye dikhaata hu
from .models import UserProfile

class UserProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields=("username","photu")

