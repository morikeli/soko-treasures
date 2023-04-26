from .models import RetailStores, Branches, Employees, Products
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
        widget=forms.URLInput(attrs={'type': 'url', 'class': 'mb-2'}),
    )
    twitter_url = forms.URLField(
        widget=forms.URLInput(attrs={'type': 'url', 'class': 'mb-2'}),
    )
    linkedin_url = forms.URLField(
        widget=forms.URLInput(attrs={'type': 'url', 'class': 'mb-2'}),
    )

    class Meta:
        model = RetailStores
        fields = ['facebook_url', 'twitter_url', 'linkedin_url']


class BranchRegistrationForm(forms.ModelForm):
    """
        This form is used to add details about a branch store.
    """
    location = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter location of this branch: Street, County/City'}),
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter P.O. Box used by your branch store'}),
    )
    image = forms.FileField(
        widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png, .svg'}),
    )

    class Meta:
        model = Branches
        fields = '__all__'


class AddEmployeesForm(forms.ModelForm):
    """
        Owners of retail stores use this form to add new employees to their retail stores.
    """
    SELECT_GENDER = (
        (None, '-- Select your gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'type': 'email', 'class': 'mb-2'}),
    )
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_GENDER,
    )
    phone_no = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel'}),
        help_text='Enter your phone number without your country code'
    )
    branch = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mt-2 mb-2', 'placeholder': 'Enter the branch of this employee'}),
        label='Branch Name',
        required=False,
    )
    role = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': "What is the employee's role in the company?"}),
        help_text='Is the employee a manager, secretary or security personnel?, etc.',
    )
    salary = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'mt-2 mb-2', 'min': 0,}),
    )
    profile_pic = forms.FileField(
        widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png, .svg'}),
    )

    class Meta:
        model = Employees
        fields = ['full_name', 'gender', 'email', 'phone_no', 'branch', 'role', 'salary', 'profile_pic']


class AddProductsForm(forms.ModelForm):
    """
        This forms is used to add products for sale in a retail store.
    """
    name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
        label='Product Name',
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Enter the description of the item ...', 'class': 'mb-2'}),
    )
    quantity = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'mb-2'}),
    )
    price = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'mb-2'}),
    )
    image = forms.FileField(
        widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png, .svg'}),
    )

    class Meta:
        model = Products
        fields = ['name', 'description', 'quantity', 'price', 'image']

    
# Forms provided for editing.
class EditRetailStoresInfoForm(forms.ModelForm):
    """
        This form is used by users who have a businness account to edit details about their retail stores.
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


class EditRetailStoreLocationandAddressForm(forms.ModelForm):
    """
        This form is used to edit details such as location, address, working hours and days of the retail store.
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


class EditRetailStoreContactandSocialsForm(forms.ModelForm):
    """
        This form is used to update social media handles of a retail store
    """
    facebook_url = forms.URLField(
        widget=forms.URLInput(attrs={'type': 'url', 'class': 'mb-2'}),
    )
    twitter_url = forms.URLField(
        widget=forms.URLInput(attrs={'type': 'url', 'class': 'mb-2'}),
    )
    linkedin_url = forms.URLField(
        widget=forms.URLInput(attrs={'type': 'url', 'class': 'mb-2'}),
    )

    class Meta:
        model = RetailStores
        fields = ['facebook_url', 'twitter_url', 'linkedin_url']


class UpdateBranchDetailsForm(forms.ModelForm):
    """
        This form is used to update details about a branch store.
    """
    location = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter location of this branch: Street, County/City'}),
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter P.O. Box used by your branch store'}),
    )
    image = forms.FileField(
        widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png, .svg'}),
    )

    class Meta:
        model = Branches
        fields = '__all__'


class UpdateEmployeesProfileForm(forms.ModelForm):
    """
        Owners of retail stores use this form to update employees' profile working in their retail stores.
    """
    SELECT_GENDER = (
        (None, '-- Select your gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'type': 'email', 'class': 'mb-2'}),
    )
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_GENDER,
    )
    phone_no = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel'}),
        help_text='Enter your phone number without your country code'
    )
    branch = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mt-2 mb-2', 'placeholder': 'Enter the branch of this employee'}),
        label='Branch Name',
        required=False,
    )
    role = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': "What is the employee's role in the company?"}),
        help_text='Is the employee a manager, secretary or security personnel?, etc.',
    )
    salary = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'mt-2 mb-2', 'min': 0,}),
    )
    profile_pic = forms.FileField(
        widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png, .svg'}),
    )

    class Meta:
        model = Employees
        fields = ['full_name', 'gender', 'email', 'phone_no', 'branch', 'role', 'salary', 'profile_pic']


class UpdateProductsForm(forms.ModelForm):
    """
        This forms is used to update products available for sale in a retail store.
    """
    name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
        label='Product Name',
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'type': 'text', 'placeholder': 'Enter the description of the item ...', 'class': 'mb-2'}),
    )
    quantity = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'mb-2'}),
    )
    price = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'mb-2'}),
    )
    image = forms.FileField(
        widget=forms.FileInput(attrs={'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png, .svg'}),
    )
    out_of_stock = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'py-2'}),
        help_text='Is this product out of stock?',
        required=True,
    )

    class Meta:
        model = Products
        fields = ['name', 'description', 'quantity', 'price', 'image']

