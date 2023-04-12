from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

INPUT_CLASSES = 'mb-2'

class SignupForm(UserCreationForm):
    SELECT_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    first_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': INPUT_CLASSES , 'autofocus': True}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': INPUT_CLASSES}), label='Surname', required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email', 'class': INPUT_CLASSES}), required=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': INPUT_CLASSES}), label='Phone Number', required=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': INPUT_CLASSES}), choices=SELECT_GENDER)
    is_shopowner = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'mt-3'}), label='Business account',
        help_text="I'm registering as a business man. <br>\
        <b>Select the checkbox if you want to create a business person account</b>")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'phone_no', 'password1', 'password2', 'is_shopowner']


class EditProfileForm(forms.ModelForm):
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': INPUT_CLASSES}), label='Phone Number', required=True)

    class Meta:
        model = User
        fields = ['phone_no', 'profile_pic']
        widgets = {
            'phone_no': forms.TextInput(attrs={'type': 'tel', 'class': INPUT_CLASSES}),
        }

