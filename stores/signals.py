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

