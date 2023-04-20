from django.db import models
from accounts.models import User
from PIL import Image


class RetailStores(models.Model):
    """
        Users who create business account, have to register their retail stores. This table will store info.
        about their retail stores.
    """
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    name = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)     # owner of the retail store
    store = models.CharField(max_length=50, blank=False)    # name of the retail store
    image = models.ImageField(upload_to='Retail-Stores/stores/imgs/', default='shop.svg')
    mobile_no_1 = models.CharField(max_length=10, blank=False)
    mobile_no_2 = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=8, blank=False)
    service = models.CharField(max_length=30, blank=False)
    opening_hours = models.TimeField(null=True, blank=False)
    closing_hours = models.TimeField(null=True, blank=False)
    working_days = models.CharField(max_length=20, blank=False)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return self.store
    
    def save(self, *args, **kwargs):
        super(RetailStores, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 600 and img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        ordering = ['name', 'location']
        verbose_name_plural = 'Retail Stores'


class Branches(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    branch = models.ForeignKey(RetailStores, on_delete=models.CASCADE, editable=False)  # branch of the retail store
    name = models.CharField(max_length=50, blank=False)     # name of the branch
    location = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=8, blank=False)
    image = models.ImageField(upload_to='Retail-Stores/branches/imgs/', default='shop.svg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Branches, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 600 and img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        ordering = ['branch', 'name', 'location']
        verbose_name_plural = 'Branches'


class Employees(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    retail_store = models.ForeignKey(RetailStores, on_delete=models.CASCADE, editable=False)
    branch = models.CharField(max_length=50, blank=True)    # employeed in which branch store
    full_name = models.CharField(max_length=50, blank=False)
    profile_pic = models.ImageField(upload_to='Retail-Stores/employees/dps/')
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=10, blank=False)
    email = models.EmailField(unique=True, blank=False)
    role = models.CharField(max_length=30, blank=False)     # role of the employee
    salary = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Employees, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    class Meta:
        ordering = ['retail_store', 'full_name']
        verbose_name_plural = 'Employees Records'
    
