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
    total_votes = models.PositiveIntegerField(default=0, editable=False)
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
    rating = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    cost = models.DecimalField(default=0, decimal_places=2, max_digits=20, editable=False)
    total_votes = models.PositiveIntegerField(default=0, editable=False)
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

class Cart(models.Model):
    id = models.CharField(primary_key=True, max_length=30, unique=True, editable=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    session_id = models.CharField(max_length=30, blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, editable=False)

    def __str__(self) -> str:
        return self.customer
    
    @property
    def get_cart_total(self):
        cart_items = self.cartitems_set.all()
        total = sum([item.get_total_cost for item in cart_items])
        return total
    
    @property
    def get_cart_items(self):
        cart_items = self.cartitems_set.all()
        total_items = sum([item.quantity for item in cart_items])
        return total_items
    
    class Meta:
        ordering = ['customer', '-date_ordered']
        verbose_name_plural = 'Cart records'
    
class CartItems(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True, editable=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, editable=False)
    order = models.ForeignKey(Cart, on_delete=models.CASCADE, editable=False)
    quantity = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product}'
    
    @property
    def get_total_cost(self):
        total_cost = self.product.price * self.quantity
        return total_cost
    
    class Meta:
        ordering = ['product', '-date_created']
        verbose_name_plural = 'Items in cart'

class Reports(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    store = models.ForeignKey(RetailStores, on_delete=models.CASCADE, editable=False)
    feedback = models.TextField()
    crime = models.CharField(max_length=30, blank=False)
    date_reported = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.store
    
    class Meta:
        ordering = ['store', '-date_reported']
        verbose_name_plural = 'Reported stores records'

class Polls(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    voter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    store = models.ForeignKey(RetailStores, on_delete=models.CASCADE, null=True, editable=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, editable=False)
    voting_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.voter
    
    class Meta:
        ordering = ['voter', 'voting_date']
        verbose_name_plural = 'Polls'

class ShippingDetails(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50, blank=False)
    mobile_no = PhoneNumberField(blank=False)
    email = models.EmailField(blank=False)
    country = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=30, blank=False, db_column='County/State')
    city = models.CharField(max_length=30, blank=False, db_column='City/Estate/Town/Village')
    address = models.CharField(max_length=10, blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name', '-date_ordered']
        verbose_name_plural = 'Customer orders records'

