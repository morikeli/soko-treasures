from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

INPUT_CLASSES = 'mb-2'

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'phone_no', 'password1', 'password2']
        widgets = {
            'first_name': forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': INPUT_CLASSES}), required=True),
            'last_name': forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': INPUT_CLASSES}), required=True),
            'username': forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': INPUT_CLASSES}), required=True),
        }


class EditProfile(forms.ModelForm):
    class User:
        model = User
        fields = ['phone_no', 'profile_pic']
        widgets = {
            'phone_no': forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': INPUT_CLASSES}), required=True)
        }

