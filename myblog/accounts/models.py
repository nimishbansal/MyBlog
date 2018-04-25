from django.conf import settings
from django.contrib.auth import get_user_model#from django.contrib.auth.models import User
from django.db import models
import os
# Create your models here.
from django.db.models.signals import post_save
from django.urls import reverse_lazy


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'profile_pics/user_{0}.{1}'.format(str(instance.user.username),filename.split(".")[1])


User=get_user_model()


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="User")
    photu = models.ImageField(upload_to=user_directory_path ,blank=True)
    following=models.ManyToManyField(User,related_name="followed_by")


    def __str__(self):
        return str(self.user)+"(profile)"

    def get_photo_url(self):
        return "profile_pics/user_{0}.png".format(self.user.username)

    def get_profile_url(self):
        return "profile_pics/user_{0}.png".format(self.user.username)



class Email(models.Model):
    email_sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name="emitter")
    email_receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name="receiver")
    title=models.CharField(max_length=100)
    email_text=models.TextField(max_length=20000)

