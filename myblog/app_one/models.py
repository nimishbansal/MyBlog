# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    title=models.CharField(validators=[MinLengthValidator(5,"atleast 5 characters")],max_length=100)
    post_id=models.AutoField(primary_key=True)
    code_text=models.TextField(validators=[MinLengthValidator(3,"atleast 3 characters")])

    def __str__(self):
        return self.title



