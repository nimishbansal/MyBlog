# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

User=get_user_model()
print(User)

class Post(models.Model):
    title=models.CharField(validators=[MinLengthValidator(5,"atleast 5 characters")],max_length=100)
    post_id=models.AutoField(primary_key=True)
    code_text=models.TextField(validators=[MinLengthValidator(3,"atleast 3 characters")])
    post_type=models.TextField(choices=[("automation","automation"),("software","software"),("android","android")])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_id=models.AutoField(primary_key=True)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="commentobject")
    comment_text=models.TextField(validators=[MinLengthValidator(3,"atleast 3 characters")])
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='userholder')
    timestamp = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.comment_text+" ("+str(self.comment_id)+")"


