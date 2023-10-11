from .models import RetailStores, Products, Reports, ShippingDetails
from .utils import validate_image_file
from django import forms

class CreateRetailStoreForm(forms.ModelForm):
    SELECT_SERVICES_OFFERED = (
        (None, '-- Select service you offer --'),
        ('Automotive', 'Automotive (Cars, motorcycles, trucks, etc.)'),
        ('Bakery', 'Bakery'),
        ('Clothing/Fashion', 'Clothing'),
        ('Cosmetics', 'Cosmetics'),
        ('Electronics', 'Electronics'),
        ('Entertainment', 'Entertainment (Games, Movies, etc.)'),
        ('Furniture', 'Furniture'),
        ('Grocery', 'Grocery'),
        ('Laundry', 'Laundry'),
        ('Restaurant', 'Restaurant'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        }),
        help_text='Enter the name of your retail store',
    )
    description = forms.CharField(widget=forms.Textarea(attrs={
            'type': 'text',
        }),
        help_text='Provide details about your store: mobile no., location, address, working days, opening/closing hours, etc.',
    )
    address = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text',
        }),
        help_text='Enter P.O. Box of your retail store.',
        required=True,
    )
    services = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-2',
        }),
        choices=SELECT_SERVICES_OFFERED,
    )
    fb_url = forms.URLField(widget=forms.URLInput(attrs={
            'type': 'url', 'class': 'mb-2',
        }),
        label='Facebook url link',
        required=False,
    )
    x_url = forms.URLField(widget=forms.URLInput(attrs={
            'type': 'url', 'class': 'mb-2',
        }),
        label='X (formerly Twitter) url link',
        required=False,
    )
    ig_url = forms.URLField(widget=forms.URLInput(attrs={
            'type': 'url', 'class': 'mb-2',
        }),
        label='Instagram url link',
        required=False,
    )

    class Meta:
        model = RetailStores
        fields = ['name', 'description', 'address', 'services', 'fb_url', 'x_url', 'ig_url']

class AddProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={
            'type': 'text',
        }),
        help_text='Provide details about this product, e.g. products specs or warranty or dimensions, etc.',
    )
    quantity = forms.FloatField(widget=forms.TextInput(attrs={
            'type': 'number', 'class': 'mb-2', 'min': '0',
        }),
        help_text='How many product do you wish to sell?'
    )
    price = forms.FloatField(widget=forms.TextInput(attrs={
            'type': 'number', 'class': 'mb-2', 'min': '0',
        }),
        help_text='How much does each item, packet or product cost?'
    )
    img_file = forms.FileField(widget=forms.FileInput(attrs={
            'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png',
        }),
        required=True,
        validators=[validate_image_file],
    )

    class Meta:
        model = Products
        fields = ['product', 'description', 'quantity', 'price', 'img_file']

class RateRetailStoreForm(forms.ModelForm):
    rating = forms.CharField(widget=forms.NumberInput(attrs={
            'type': 'number', 'class': 'mb-0', 'min': 0, 'max': 5,
        }),
        required=True,
        help_text='Enter your rate score.'
    )
    class Meta:
        model = RetailStores
        fields = ['rating']

class RateProductsForm(forms.ModelForm):
    rating = forms.CharField(widget=forms.NumberInput(attrs={
            'type': 'number', 'class': 'mb-0', 'min': 0, 'max': 5,
        }),
        required=True,
        help_text='Enter your rate score.'
    )
    class Meta:
        model = Products
        fields = ['rating']

class ReportRetailStoreForm(forms.ModelForm):
    SELECT_TYPE_OF_CRIME = (
        (None, '-- Select crime choice --'),
        ('Con', 'It\'s a con business'),
        ('Drugs', 'Selling drugs'),
        ('Fraud', 'Fraud'),
        ('Other', 'Other'),
    )
   
    crime = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-2',
        }),
        choices=SELECT_TYPE_OF_CRIME,
    )

    feedback = forms.CharField(widget=forms.Textarea(attrs={
            'type': 'text', 'class': 'mb-0', 
        }),
        help_text='Provide any additional you have about the selected crime.',
        required=True,
    )

    class Meta:
        model = Reports
        fields = ['crime', 'feedback']

class CustomerOrderForm(forms.ModelForm):
    SELECT_COUNTRY_OF_ORIGIN = (
        (None, '-- Select country --'),
        ('Kenya', 'Kenya'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-0',
        }),
        label='Full name',
        required=True,
    )
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'tel', 'class': 'mb-0',
        }),
        help_text='Enter your mobile number and include your country code, e.g. +254112345678',
        required=True,
        label='Mobile number',
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            'type': 'email', 'class': 'mb-0',
        }),
        required=True,
        label='Email address',
    )
    country = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'text', 'class': 'mb-0',
        }),
        required=True,
        help_text='Select current residential country.',
        choices=SELECT_COUNTRY_OF_ORIGIN,
    )
    county = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-0',
        }),
        required=True,
        help_text='Select current residential county/state.',
    )
    city = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-0',
        }),
        required=True,
        help_text='Select current residential city/estate/town/village.',
    )
    address = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-0',
        }),
        required=True,
        help_text='Enter your P.O. Box or zip code.'
    )
    
    class Meta:
        model = ShippingDetails
        fields = ['name', 'email', 'mobile_no', 'country', 'county', 'city', 'address']

# Edit forms
class EditStoreInfoForm(forms.ModelForm):
    SELECT_SERVICES_OFFERED = (
        (None, '-- Select service you offer --'),
         ('Automotive', 'Automotive (Cars, motorcycles, trucks, etc.)'),
        ('Bakery', 'Bakery'),
        ('Clothing/Fashion', 'Clothing'),
        ('Cosmetics', 'Cosmetics'),
        ('Electronics', 'Electronics'),
        ('Entertainment', 'Entertainment (Games, Movies, etc.)'),
        ('Furniture', 'Furniture'),
        ('Grocery', 'Grocery'),
        ('Laundry', 'Laundry'),
        ('Restaurant', 'Restaurant'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        }),
        help_text='Enter the name of your retail store',
        disabled=True,
    )
    description = forms.CharField(widget=forms.Textarea(attrs={
            'type': 'text',
        }),
        help_text='Provide details about your store: mobile no., location, address, working days, opening/closing hours, etc.',
    )
    address = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text',
        }),
        help_text='Enter P.O. Box of your retail store.',
    )
    services = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-2',
        }),
        choices=SELECT_SERVICES_OFFERED,
    )
    fb_url = forms.URLField(widget=forms.URLInput(attrs={
            'type': 'url', 'class': 'mb-2',
        }),
        label='Facebook url link',
        required=False,
    )
    x_url = forms.URLField(widget=forms.URLInput(attrs={
            'type': 'url', 'class': 'mb-2',
        }),
        label='X (formerly Twitter) url link',
        required=False,
    )
    ig_url = forms.URLField(widget=forms.URLInput(attrs={
            'type': 'url', 'class': 'mb-2',
        }),
        label='Instagram url link',
        required=False,
    )
    image = forms.FileField(widget=forms.FileInput(attrs={
            'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png',
        }),
        required=True,
        validators=[validate_image_file],
    )
    cover_photo = forms.FileField(widget=forms.FileInput(attrs={
            'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png',
        }),
        required=False,
        validators=[validate_image_file],
    )

    class Meta:
        model = RetailStores
        fields = ['name', 'description', 'address', 'services', 'fb_url', 'x_url', 'ig_url', 'image', 'cover_photo']

class EditProductInfoForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={
            'type': 'text',
        }),
        help_text='Provide details about this product, e.g. products specs or warranty or dimensions, etc.',
    )
    quantity = forms.FloatField(widget=forms.TextInput(attrs={
            'type': 'number', 'class': 'mb-2', 'min': '0',
        }),
        help_text='How many product do you wish to sell?'
    )
    price = forms.FloatField(widget=forms.TextInput(attrs={
            'type': 'number', 'class': 'mb-2', 'min': '0',
        }),
        help_text='How much does each item, packet or product cost?'
    )
    img_file = forms.FileField(widget=forms.FileInput(attrs={
            'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png',
        }),
        required=False,
        validators=[validate_image_file],
    )

    class Meta:
        model = Products
        fields = ['product', 'description', 'quantity', 'price', 'img_file']