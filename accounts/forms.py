from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm
from .utils import validate_image_file
from .models import User
from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text',
        }),
        label='Email',
    )
    store_name = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text',
        })
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'type': 'password',
        })
    )

class SignupForm(UserCreationForm):
    SELECT_GENDER = (
        (None, '-- Select your gender --'),
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    SELECT_COUNTRY = (
        (None, '-- Select your country of origin --'),
        ('Kenya', 'Kenya'),
    )
    first_name = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-2', 'autofocus': True
        }),
        required=True,
    )
    last_name = forms.CharField(widget=forms.TextInput(attrs={
           'type': 'text', 'class': 'mb-2',
        }),
        required=True,
    )
    username = forms.CharField(widget=forms.TextInput(attrs={
           'type': 'text', 'class': 'mb-2',
        }),
        required=True,
    )
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'tel', 'class': 'mb-0',
        }),
        help_text='Enter your phone number and include your country code, e.g. +254112345678'
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': 'email', 'class': 'mb-2',
        }),
    )
    gender = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-2',
        }),
        choices=SELECT_GENDER,
    )
    dob = forms.DateField(widget=forms.DateInput(attrs={
            'type': 'date', 'class': 'mb-2',
        }),
        required=True,
    )
    country = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-2'
        }),
        choices=SELECT_COUNTRY,
        required=True,
        label='Country of origin',
    )
    national_id = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'mb-2', 'maxlength': '8',
        }),
        required=True,
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'mobile_no', 'gender', 'dob', 'country', 'national_id',
        ]
    
class EditProfileForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select your gender --'),
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    SELECT_COUNTRY = (
        (None, '-- Select your country of origin --'),
        ('Kenya', 'Kenya'),
    )

    first_name = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-2', 'autofocus': True
        }),
        required=True,
        disabled=True,
    )
    last_name = forms.CharField(widget=forms.TextInput(attrs={
           'type': 'text', 'class': 'mb-2',
        }),
        required=True,
        disabled=True,
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': 'email', 'class': 'mb-2',
        }),
    )
    gender = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-2',
        }),
        choices=SELECT_GENDER,
        disabled=True,
    )
    dob = forms.DateField(widget=forms.DateInput(attrs={
            'type': 'date', 'class': 'mb-2',
        }),
        required=True,
        disabled=True,
    )
    country = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-2'
        }),
        choices=SELECT_COUNTRY,
        required=True,
        disabled=True,
        label='Country of origin',
    )
    national_id = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'mb-2',
        }),
        required=True,
        disabled=True,
        label='National ID No.',
    )
    profile_pic = forms.FileField(
        widget=forms.FileInput(attrs={
            'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png',
        }),
        required=False,
        validators=[validate_image_file],
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'gender', 'dob',
            'country', 'national_id', 'mobile_no', 'profile_pic',
        ]