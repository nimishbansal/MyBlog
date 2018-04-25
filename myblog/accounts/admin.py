from django.contrib import admin
from .models import UserProfile,Email
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Email)