from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

INPUT_CLASSES = 'mb-2'

class SignupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': INPUT_CLASSES , 'autofocus': True}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': INPUT_CLASSES}), label='Surname', required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email', 'class': INPUT_CLASSES}), required=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': INPUT_CLASSES}), label='Phone Number', required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'phone_no', 'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': INPUT_CLASSES}), label='Phone Number', required=True)

    class Meta:
        model = User
        fields = ['phone_no', 'profile_pic']
        widgets = {
            'phone_no': forms.TextInput(attrs={'type': 'tel', 'class': INPUT_CLASSES}),
        }

