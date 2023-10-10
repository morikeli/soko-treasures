from .models import RetailStores, Products, Cart
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

    class Meta:
        model = RetailStores
        fields = []

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