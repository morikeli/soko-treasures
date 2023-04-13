from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

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

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        dp = Image.open(self.profile_pic.path)

        if dp.height > 480 and dp.width > 480:
            output_size = (480, 480)
            dp.thumbnail(output_size)
            dp.save(self.profile_pic.path)
    

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
    

