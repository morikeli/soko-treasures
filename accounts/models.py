from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, blank=False)
    phone_no = models.CharField(max_length=10, blank=False)
    national_id = models.CharField(max_length=8, blank=True)
    profile_pic = models.ImageField(upload_to='User-dps/', default='default.png')
    is_shopowner = models.BooleanField(default=False, editable=True)
    updated = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
    

