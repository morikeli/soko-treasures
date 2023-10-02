from .models import RetailStores, Products, Orders
from .utils import validate_image_file
from django import forms

class CreateRetailStoreForm(forms.ModelForm):
    SELECT_SERVICES_OFFERED = (
        (None, '-- Select service you offer --'),
        ('Automotive', 'Automotive (Cars, motorcycles, trucks, etc.)'),
        ('Clothing/Fashion', 'Clothing'),
        ('Electronics', 'Electronics'),
        ('Entertainment', 'Entertainment (Games, Movies, etc.)'),
        ('Furniture', 'Furniture'),
        ('Grocery', 'Grocery'),
        ('Laundry', 'Laundry'),
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
        fields = ['name', 'description', 'services', 'fb_url', 'x_url', 'ig_url', 'image']

class AddProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={
            'type': 'text',
        }),
        help_text='Provide details about this product, e.g. products specs or warranty or dimensions, etc.',
    )
    quantity = forms.FloatField(widget=forms.TextInput(attrs={
            'type': 'number', 'class': 'mb-2', 'min': '0',
        }),
    )
    price = forms.FloatField(widget=forms.TextInput(attrs={
            'type': 'number', 'class': 'mb-2', 'min': '0',
        }),
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


class PlaceOrderForm(forms.ModelForm):
    customer = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-0',
        }),
        help_text='Enter your full name',
        required=True,
    )
    item = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text', 'class': 'mb-2',
        }),
        disabled=True,
    )
    quantity = forms.FloatField(widget=forms.NumberInput(attrs={
            'type': 'number', 'class': 'mb-0', 'min': 0,
        }),
        help_text='Enter number of item(s) you wish to order',
    )
    price = forms.FloatField(widget=forms.NumberInput(attrs={
            'type': 'number', 'class': 'mb-0',
        }),
        help_text='Price of each item',
        disabled=True,
    )

    class Meta:
        model = Orders
        fields = ['customer', 'item', 'quantity', 'price']


# Edit forms
class EditStoreInfoForm(forms.ModelForm):
    SELECT_SERVICES_OFFERED = (
        (None, '-- Select service you offer --'),
        ('Automotive', 'Automotive (Cars, motorcycles, trucks, etc.)'),
        ('Clothing/Fashion', 'Clothing'),
        ('Electronics', 'Electronics'),
        ('Entertainment', 'Entertainment (Games, Movies, etc.)'),
        ('Furniture', 'Furniture'),
        ('Grocery', 'Grocery'),
        ('Laundry', 'Laundry'),
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
    services = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-2',
        }),
        choices=SELECT_SERVICES_OFFERED,
    )
    fb_url = forms.URLField(widget=forms.URLInput(attrs={
            'type': 'url', 'class': 'mb-2',
        }),
        label='Facebook url link',
    )
    x_url = forms.URLField(widget=forms.URLInput(attrs={
            'type': 'url', 'class': 'mb-2',
        }),
        label='X (formerly Twitter) url link',
    )
    ig_url = forms.URLField(widget=forms.URLInput(attrs={
            'type': 'url', 'class': 'mb-2',
        }),
        label='Instagram url link',
    )
    image = forms.FileField(widget=forms.FileInput(attrs={
            'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png',
        }),
        required=False,
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
        fields = ['name', 'description', 'services', 'fb_url', 'x_url', 'ig_url', 'image']

class EditProductInfoForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={
            'type': 'text',
        }),
        help_text='Provide details about this product, e.g. products specs or warranty or dimensions, etc.',
    )
    quantity = forms.FloatField(widget=forms.TextInput(attrs={
            'type': 'number', 'class': 'mb-2', 'min': '0',
        }),
    )
    price = forms.FloatField(widget=forms.TextInput(attrs={
            'type': 'number', 'class': 'mb-2', 'min': '0',
        }),
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