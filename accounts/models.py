from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

class User(AbstractUser):
    """ This is a custom user model. Its the user model used for user profile and auth. """
    id = models.CharField(max_length=25, primary_key=True, editable=False, unique=True)
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(max_length=7, blank=False)
    dob = models.DateTimeField(blank=False, null=True)
    age = models.PositiveIntegerField(editable=False)
    country = models.CharField(max_length=70, blank=False)
    national_id = models.PositiveIntegerField(blank=False)
    mobile_no = PhoneNumberField(blank=False)
    profile_pic = models.ImageField(upload_to='Users/dps/', default='default.png')
    updated = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 500 and img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['first_name', 'last_name', 'username']
    
