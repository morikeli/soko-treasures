from .models import RetailStore, Stock, Branches, Employees
from django import forms


class RetailStoreInfoForm(forms.ModelForm):
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
    name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text',}),
        help_text='Enter the name of your retail store',
        )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'type': 'text', 'class': 'mt-2 mb-2'}),
        help_text='Provide a brief summary of the services your store offers',
        )
    service = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_SERVICE_OFFERED,
        )

    class Meta:
        model = RetailStore
        fields = ['name', 'description', 'service', 'image']


class RetailStoreLocationForm(forms.ModelForm):
    SELECT_WORKING_DAYS = (
        (None, '-- Select working days --'),
        ('Sun - Fri', 'Sun - Fri'),
        ('Mon - Fri', 'Mon - Fri'),
        ('Mon - Sat', 'Mon - Sat'),
        ('24/7/365', '24/7/365'),
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
        help_text='Enter street and postal address of your business, e.g. <b>"Example Street, Nairobi"</b>',
        )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
        help_text='Enter postal address used by your store/business, e.g. 01-0101, 02-234',
        )
    opening_hours = forms.CharField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'mb-2'}),
        )
    closing_hours = forms.CharField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'mb-2'}),
        help_text='Enter time in 24-hr clock system',
        )
    working_days = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_WORKING_DAYS,
        )

    class Meta:
        model = RetailStore
        fields = ['location', 'address', 'opening_hours', 'closing_hours', 'working_days']


class RetailStoreContactsandSocialLinksForm(forms.ModelForm):
    mobile_no_1 = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}),
        )
    mobile_no_2 = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}),
        required=False,
        )
    
    class Meta:
        model = RetailStore
        fields = ['mobile_no_1', 'mobile_no_2', 'facebook_url', 'instagram_url', 'linkedin_url']
        

class AddNewStockForm(forms.ModelForm):
    item = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text'}),
        help_text='Enter the name of the product you want to add',
        )
    quantity = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'mt-2 mb-2'}),
        help_text='Enter the quantity of the item, e.g. 2, 10, 100, 500',
        )
    price = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'mb-2'}),
        help_text='Enter the price of each item',
        )

    class Meta:
        model = Stock
        fields = ['item', 'quantity', 'price', 'img']


class AddNewRetailStoreBranchForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
        help_text='Enter street and postal address of your the branch store, e.g. <b>"Example Street, Mombasa"</b>',
        )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
        help_text='Enter postal address and postal code used by the branch store, e.g. 01-0101, 02-234',
        )

    class Meta:
        model = Branches
        fields = ['location', 'address', 'image']


class AddNewEmployeeForm(forms.ModelForm):
    employee = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
        help_text='Enter the full name of an employee',
        )
    salary = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'mt-1', 'min': '0', 'max': '100000000'}),
        required=True, help_text='Enter the salary of this employee',
        )
    role = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'mt-1'}),
        required=True,
        help_text='Is he/she a supervisor, secretary, manager or a security officer?',
        )

    class Meta:
        model = Employees
        fields = ['employee', 'salary', 'role']


# forms to edit info.
class UpdateRetailStoreInfoForm(forms.ModelForm):
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
    name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text',}),
        help_text='Enter the name of your retail store',
        )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'type': 'text', 'class': 'mt-2 mb-2'}),
        help_text='Provide a brief summary of the services your store offers',
        )
    service = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_SERVICE_OFFERED,
        )

    class Meta:
        model = RetailStore
        fields = ['name', 'description', 'service', 'image']


class UpdateRetailStoreLocationForm(forms.ModelForm):
    SELECT_WORKING_DAYS = (
        (None, '-- Select working days --'),
        ('Sun - Fri', 'Sun - Fri'),
        ('Mon - Fri', 'Mon - Fri'),
        ('Mon - Sat', 'Mon - Sat'),
        ('24/7/365', '24/7/365'),
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
        help_text='Enter street and postal address of your business, e.g. <b>"Example Street, Nairobi"</b>',
        )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
        help_text='Enter postal address used by your store/business, e.g. 01-0101, 02-234',
        )
    opening_hours = forms.CharField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'mb-2'}),
        )
    closing_hours = forms.CharField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'mb-2'}),
        help_text='Enter time in 24-hr clock system',
        )
    working_days = forms.ChoiceField(
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}),
        choices=SELECT_WORKING_DAYS,
        )

    class Meta:
        model = RetailStore
        fields = ['location', 'address', 'opening_hours', 'closing_hours', 'working_days']


class UpdateRetailStoreContactsandSocialLinksForm(forms.ModelForm):
    mobile_no_1 = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}),
        )
    mobile_no_2 = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}),
        required=False,
        )
    
    class Meta:
        model = RetailStore
        fields = ['mobile_no_1', 'mobile_no_2', 'facebook_url', 'instagram_url', 'linkedin_url']


class EditStockItemForm(forms.ModelForm):
    item = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text'}),
        help_text='Enter the name of the product you want to add',
        )
    quantity = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'mt-2 mb-2'}),
        help_text='Enter the quantity of the item, e.g. 2, 10, 100, 500',
        )
    price = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'mb-2'}),
        help_text='Enter the price of each item',
        )

    class Meta:
        model = Stock
        fields = ['item', 'quantity', 'price', 'img', 'out_of_stock']


class EditRetailStoreBranchForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
        help_text='Enter street and postal address of your the branch store, e.g. <b>"Example Street, Mombasa"</b>',
        )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}),
        help_text='Enter postal address and postal code used by the branch store, e.g. 01-0101, 02-234',
        )

    class Meta:
        model = Branches
        fields = ['location', 'address', 'image']


class EditEmployeeDetailsForm(forms.ModelForm):
    salary = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'select', 'min': '0', 'max': '100000000'}),
        required=True,
        help_text='Enter the salary of this employee',
        )
    role = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text'}),
        required=True,
        help_text='Is he/she a supervisor, secretary, manager or a security officer?'
        )

    class Meta:
        model = Employees
        fields = ['employee', 'salary', 'role']

