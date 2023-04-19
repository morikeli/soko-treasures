from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Products, Transactions, PaidOrders
import uuid


@receiver(pre_save, sender=Products)
def generate_productsID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]

@receiver(pre_save, sender=Transactions)
def generate_transactionID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]

@receiver(pre_save, sender=PaidOrders)
def generate_paid_ordersID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]
