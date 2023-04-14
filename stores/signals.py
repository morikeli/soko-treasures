from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import RetailStore, Stock, Transactions, Branches, Employees
import uuid


@receiver(pre_save, sender=RetailStore)
def generate_storesID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]

@receiver(pre_save, sender=Branches)
def generate_branchID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]

@receiver(pre_save, sender=Employees)
def generate_employeeID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]

@receiver(pre_save, sender=Stock)
def generate_stockID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]

@receiver(pre_save, sender=Transactions)
def generate_transactionID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:30]

