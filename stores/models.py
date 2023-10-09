from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import User
from django.db import models
from PIL import Image

class RetailStores(models.Model):
    id = models.CharField(primary_key=True, max_length=25, unique=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)   # owner of the retail store
    name = models.CharField(max_length=60, blank=False)   # name of the retail store
    description = models.TextField()
    services = models.CharField(max_length=50, blank=False, db_column='Services offered')
    address = models.CharField(max_length=40, blank=False)
    rating = models.PositiveIntegerField(default=0)
    fb_url = models.URLField(blank=True)
    x_url = models.URLField(blank=True)
    ig_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='Retail-Stores/imgs/', default='shop.jpg')
    cover_photo = models.ImageField(upload_to='Retail-Stores/imgs/cover-photos/', default='cover-photo.jpg')    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(RetailStores, self).save(*args, **kwargs)

        # resize retail store's image file
        img = Image.open(self.image.path)
        
        output_size = (640, 480)
        img.thumbnail(output_size)
        img.save(self.image.path)
        
        # resize retail store's cover photo used in stores template -> templates/stores.html
        cover_img = Image.open(self.cover_photo.path)
        
        output_size = (1280, 720)
        cover_img.thumbnail(output_size)
        cover_img.save(self.cover_photo.path)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Retail Stores'


class Products(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True, editable=False)
    seller = models.ForeignKey(RetailStores, on_delete=models.CASCADE, editable=False)
    product = models.CharField(max_length=70, blank=False, db_column='Product Name')  # name of the product
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0.00)
    cost = models.FloatField(default=0.00, editable=False)
    img_file = models.ImageField(upload_to='Products/imgs/', default='cart.jpeg')
    out_of_stock = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product
    
    def save(self, *args, **kwargs):
        super(Products, self).save(*args, **kwargs)

        img = Image.open(self.img_file.path)

        output_size = (640, 480)
        img.thumbnail(output_size, reducing_gap=2.0)
        img.save(self.img_file.path)
    
    class Meta:
        ordering = ['seller', 'product']
        verbose_name_plural = 'Products'

class Orders(models.Model):
    id = models.CharField(primary_key=True, max_length=20, unique=True, editable=False)
    store_name = models.ForeignKey(RetailStores, on_delete=models.CASCADE, editable=False, db_column='Retail store')
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.CharField(max_length=50, blank=False)
    phone_no = PhoneNumberField(blank=False)
    address = models.CharField(max_length=20, blank=False)
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)
    total_cost = models.FloatField(default=0, editable=False)
    paid = models.BooleanField(default=False, editable=False)   # has the user paid for the product?
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer}'

    class Meta:
        ordering = ['customer', '-created']
        verbose_name_plural = 'Customer orders'

class CartItems(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=False, editable=False)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    item = models.ForeignKey(Products, on_delete=models.CASCADE, editable=False)
    session_id = models.CharField(max_length=50, blank=False, editable=False)
    is_paid = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f''
    
    class Meta:
        verbose_name_plural = 'Cart items'
        ordering = []