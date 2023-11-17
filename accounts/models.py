from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Customized user model
class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=13, unique=True)
    user_profile_image = models.ImageField(upload_to='profile_image')
    user_bio = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"   #USERNAME_FIELD could be single value only
    REQUIRED_FIELDS =[]


    # class Meta:
    #     swappable = "AUTH_USER_MODEL"

