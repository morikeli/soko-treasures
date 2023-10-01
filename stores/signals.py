from django.db.models.signals import pre_save
from .models import RetailStores, Products
from django.dispatch import receiver
from uuid import uuid4

@receiver(pre_save, sender=RetailStores)
def generate_storeID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid4()).replace('-', '')[:25]

@receiver(pre_save, sender=Products)
def generate_productsID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid4()).replace('-', '')[:30]
    
    # calculate the cost of the items.
    # If the quantity of the product is 10 and each has a price $10 then the cost is $100/= (10 items x $10/=)
    if instance.cost or instance.cost == 0:
        instance.cost = instance.price * instance.quantity
