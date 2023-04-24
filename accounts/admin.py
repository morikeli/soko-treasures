from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.db import models
from .forms import SignupForm
from .models import User


class UsersLayout(UserAdmin):
    model = User
    add_form = SignupForm
    list_display = ['username', 'gender', 'country', 'is_businessaccount']
    readonly_fields = ['gender', 'phone_no', 'dob', 'national_id', 'country', 'city', 'is_businessaccount', 'profile_pic']
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget}
    }

admin.site.register(User, UsersLayout)