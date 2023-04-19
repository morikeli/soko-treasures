from accounts.models import User
from stores.models import Stock
from django.db import models


class Orders(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    item = models.ForeignKey(Stock, on_delete=models.CASCADE, editable=False)
    quantity = models.PositiveIntegerField(default=1, editable=False)
    price = models.PositiveIntegerField(default=0, editable=False)
    cost = models.PositiveIntegerField(default=0, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.buyer}'

    class Meta:
        ordering = ['buyer']
        verbose_name_plural = 'Customers Orders'

class Payments(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True, editable=False)
    client = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client}'
    
    