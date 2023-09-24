from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import User
from uuid import uuid4

@receiver(pre_save, sender=User)
def generate_userID(sender, instance, *args, **kwargs):
    if instance.id == '':
        instance.id = str(uuid4()).replace('-', '')[:25]

