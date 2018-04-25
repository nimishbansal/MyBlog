from django.conf import settings
from django.contrib.auth import get_user_model#from django.contrib.auth.models import User
from django.db import models
import os
# Create your models here.
from django.db.models.signals import post_save


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'profile_pics/user_{0}/{1}'.format(instance.user.username, filename)


User=get_user_model()

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="User")
    photu = models.ImageField(upload_to=user_directory_path ,blank=True)


#