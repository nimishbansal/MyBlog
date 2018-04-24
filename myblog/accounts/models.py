from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User=get_user_model()
#signup form upe
class UserProfile(User):
    user=models.OneToOneField(User,on_delete=models.CASCADE,parent_link=True)
    photu = models.ImageField(upload_to="profile_pics",blank=True)


#ruk