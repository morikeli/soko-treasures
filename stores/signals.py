from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import RetailStores, Branches, Employees
import uuid

@receiver(pre_save, sender=RetailStores)
def generate_storeID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]

@receiver(pre_save, sender=Branches)
def generate_branchesID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]

@receiver(pre_save, sender=Employees)
def generate_employeesID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]
