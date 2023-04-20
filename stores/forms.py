from .models import RetailStores, Branches, Employees
from django import forms


# forms to register retail stores
# For better user experience, if the info to fill in details about your retail store were place in one form,
# the form would be too large an long. Therefore the registration form is sub-divided into 3 forms:
# RetailStoreInfoForm, RetailStoreLocationandAddressForm and RetailStoreContactandSocialsForm

class RetailStoresInfoForm(forms.ModelForm):
    """
        This form is used by users who have a businness account to add details about their retail stores.
    """
    SELECT_SERVICE_OFFERED = (
        (None, '-- Select service offered --'),
        ('Automotive', 'Automotive'),
        ('Barber shop', 'Barber shop'),
        ('Cafe', 'Cafe'),
        ('Chemist', 'Chemist'),
        ('Clothing', 'Clothing'),
        ('Cosmetics', 'Cosmetics'),
        ('Cyber cafe', 'Cyber cafe'),
        ('Electronics', 'Electronics'),
        ('Entertainment', 'Entertainment'),
        ('Furniture', 'Furniture'),
        ('Salon', 'Salon'),
        ('Studio', 'Studio'),
    )

    store = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter the name of your store', 'class': 'mb-2'}),
        label='Name of your retail store',
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Type your shop description here'}),
        help_text='You can add a bio/description about your retail store/shop',
        required=False,
    )
    service = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2 mb-2'}),
        choices=SELECT_SERVICE_OFFERED,
    )
    image = forms.FileField(
        widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png, .svg'}),
    )

    class Meta:
        model = RetailStores
        fields = ['store', 'description', 'service', 'image']

class RetailStoreLocationandAddressForm(forms.ModelForm):
    """
        This form is used to add details such as location, address, working hours and days of the retail store.
    """
    SELECT_WORKING_DAYS = (
        (None, '-- Select your working days'),
        ('Mon - Fri', 'Mon - Fri'),
        ('Mon - Sat', 'Mon - Sat'),
        ('Sun - Fri', 'Sun - Fri'),
        ('24/7/365', '24/7/365'),
    )

    location = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter location: Street, County/City'}),
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter P.O. Box used by your retail store'}),
    )
    opening_hours = forms.TimeField(
        widget=forms.TextInput(attrs={'type': 'time', 'class': 'mb-2'}),
    )
    closing_hours = forms.TimeField(
        widget=forms.TextInput(attrs={'type': 'time',}),
        help_text='Enter time in 24-hr clock format',
    )
    working_days = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mt-2 mb-2'}),
        choices=SELECT_WORKING_DAYS,
    )

    class Meta:
        model = RetailStores
        fields = ['location', 'address', 'opening_hours', 'closing_hours', 'working_days']


class RetailStoreContactandSocialsForm(forms.ModelForm):
    """
        This form is used to add social media handles of a retail store
    """
    facebook_url = forms.URLField(
        forms.URLInput(attrs={'type': 'url', 'class': 'mb-2'}),
    )
    twitter_url = forms.URLField(
        forms.URLInput(attrs={'type': 'url', 'class': 'mb-2'}),
    )
    linkedin_url = forms.URLField(
        forms.URLInput(attrs={'type': 'url', 'class': 'mb-2'}),
    )

    class Meta:
        model = RetailStores
        fields = ['facebook_url', 'twitter_url', 'linkedin_url']

