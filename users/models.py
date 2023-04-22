from django.db import models
from accounts.models import User
from PIL import Image


class Products(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=False)
    price = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0, editable=False)
    image = models.ImageField(upload_to='Products/Users/', default='cart.png')
    out_of_stock = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Products, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        ordering = ['seller', 'name']
        verbose_name_plural = 'Users products'
    

class Transactions(models.Model):
    """
        This model store info. about personal transactions the used made, i.e. goods bought from
        a vendor. 
    """
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    item = models.ForeignKey(Products, on_delete=models.CASCADE, editable=False)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    payment = models.CharField(max_length=6, blank=False)   # paid via MPESA or cash
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item}'
    
    class Meta:
        ordering = ['item', '-created']
        verbose_name_plural = 'User transactions'

class PaidOrders(models.Model):
    """
        This model stores details about products bought from a given user, e.g. if user1 sold a product1,
        store details about the bought product1.
    """
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    item = models.ForeignKey(Products, on_delete=models.CASCADE, editable=False)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    payment = models.CharField(max_length=6, blank=False)   # paid via MPESA or cash
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item}'
    
    class Meta:
        ordering = ['item', '-created']
        verbose_name_plural = 'User paid orders'