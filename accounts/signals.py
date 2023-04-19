from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import User
from datetime import datetime
import uuid


@receiver(pre_save, sender=User)
def generate_userID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4()).replace('-', '')[:25]
    
    try:
        if instance.is_superuser is False and instance.is_staff is False:
            if datetime.now().strftime('%Y-%m-%d %H:%M:%S') > instance.date_joined.strftime('%Y-%m-%d %H:%M:%S'):
                user_dob = str(instance.dob)
                dob = datetime.strptime(user_dob, '%Y-%m-%d')
                current_date = datetime.now()
                users_age = current_date - dob
                convert_usersAge = int(users_age.days/365.25)
                instance.age = convert_usersAge
                
            else:
                user_dob = str(instance.dob)
                dob = datetime.strptime(user_dob, '%Y-%m-%d')
                current_date = datetime.now()
                users_age = current_date - dob
                convert_usersAge = int(users_age.days/365.25)
                instance.age = convert_usersAge

        return

    except AttributeError:
        return
