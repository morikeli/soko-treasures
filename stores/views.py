from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import (
    RetailStoreInfoForm, RetailStoreLocationForm, RetailStoreContactsandSocialLinksForm, AddNewStockForm, UpdateRetailStoreInfoForm,
    UpdateRetailStoreLocationForm, UpdateRetailStoreContactsandSocialLinksForm, EditStockItemForm, AddNewEmployeeForm, EditEmployeeDetailsForm,
    AddNewRetailStoreBranchForm, EditRetailStoreBranchForm,
    )
from .models import RetailStore, Stock, Employees, Branches
from accounts.models import User


@login_required(login_url='user_login')
def homepage_view(request, staff_member):
    staff = User.objects.get(username=staff_member, is_shopowner=True)
    url_obj = RetailStore.objects.get(owner=request.user).id    # to be used in url tags in base template. Ref. context = {} in employees_view(request).
    store_obj = RetailStore.objects.get(id=url_obj)

    # Calculations
    
    # Sales
    # total_sales

    # Stock -> Available products (still in stock)
    products = Stock.objects.filter(store=url_obj, out_of_stock=False).all().count()
     

    context = {
        'staff': staff, 'url_obj': url_obj, 'store_obj': store_obj,
        'products': products,

        }
    return render(request, 'dashboard/homepage.html', context)

@login_required(login_url='user_login')
def retails_stores_branches_view(request, store):
    branch_store = RetailStore.objects.get(id=store)
    retail_store_branches = Branches.objects.filter(branch=branch_store).all().order_by('branch')

    branch_form = AddNewRetailStoreBranchForm()
    edit_branch_form = EditRetailStoreBranchForm(instance=branch_store)

    if request.method == 'POST':
        branch_form = AddNewRetailStoreBranchForm(request.POST, request.FILES)
        edit_branch_form = EditRetailStoreBranchForm(request.POST, request.FILES, instance=branch_store)

        if branch_form.is_valid():
            new_branch = branch_form.save(commit=False)
            new_branch.branch_id = branch_store
            new_branch.branch = branch_store
            new_branch.save()

            messages.success(request, 'Branch info. successfully saved!')
            return redirect('branches', store)
        
        elif edit_branch_form.is_valid():
            edit_branch_form.save()

            messages.info(request, 'Branch details successfully updated and saved!')
            return redirect('branches', store)

    context = {
        'retail_store_branches': retail_store_branches,
        'AddNewBranchForm': branch_form, 'EditBranchDetailsForm': edit_branch_form,
        'url_obj': store, 'store_obj': branch_store,
        }
    return render(request, 'dashboard/branches.html', context)

@login_required(login_url='user_login')
def employees_view(request, store):
    store_obj = RetailStore.objects.get(id=store)
    employees = Employees.objects.filter(store_id=store_obj).all().order_by('employee')
    add_employee_form = AddNewEmployeeForm()

    try:
        # add code to update employee details
        pass


    except Employees.DoesNotExist:
        pass

    if request.method == 'POST':
        add_employee_form = AddNewEmployeeForm(request.POST)

        if add_employee_form.is_valid():
            employee_record = add_employee_form.save(commit=False)  # new employee record
            employee_record.store = store_obj
            employee_record.save()

            messages.success(request, 'Employee details successfully saved')
            return redirect('employees', store)

    context = {
        'employees': employees, 'AddNewEmployeeForm': add_employee_form,
        
        # url_obj is used in url tags in base template while store_obj is used in specified templates, in this case, employees.html
        # using store_obj in url tags raises a NoReverseMatch Error.
        'url_obj': store, 
        'store_obj': store_obj,

        }
    return render(request, 'dashboard/employees.html', context)

@login_required(login_url='user_login')
def stock_records_view(request, store):
    store_obj = RetailStore.objects.get(id=store)
    items = Stock.objects.filter(store_id=store_obj).all().order_by('item')  # products available in stock
    add_items_form = AddNewStockForm()  # form to add new item in a given retail store

    if request.method == 'POST':
        add_items_form = AddNewStockForm(request.POST, request.FILES)

        if add_items_form.is_valid():
            product_record = add_items_form.save(commit=False)
            product_record.store = store_obj

            # calculate cost of the item
            product_record.cost = product_record.quantity * product_record.price
            product_record.save()

            messages.success(request, 'Product successfully saved!')
            return redirect('add_products', store)

    context = {'items': items, 'url_obj': store, 'AddNewItemsToStockForm': add_items_form, 'store_obj': store_obj}
    return render(request, 'dashboard/stock-records.html', context)

@login_required(login_url='user_login')
def stores_view(request):

    context = {}
    return render(request, 'dashboard/stores.html', context)

def transactions_view(request):

    context = {}
    return render(request, 'dashboard/transactions.html', context)

@login_required(login_url='user_login')
def store_registration_view(request):
    store_info_form = RetailStoreInfoForm()
    store_location_form = RetailStoreLocationForm()
    store_contact_form = RetailStoreContactsandSocialLinksForm()

    if request.method == 'POST':
        store_info_form = RetailStoreInfoForm(request.POST, request.FILES)

        # save store_info_form details in database
        # Once they are stored use RetailStore.owner as the obj and use CRUD in store_location_form and store_contact_form
        # to update RetailStore details
        try:
            obj = RetailStore.objects.get(owner=request.user)
            store_location_form = RetailStoreLocationForm(request.POST, instance=obj)
            store_contact_form = RetailStoreContactsandSocialLinksForm(request.POST, instance=obj)
        except RetailStore.DoesNotExist:
            pass

        if store_info_form.is_valid():
            new_store = store_info_form.save(commit=False)
            new_store.owner = request.user
            new_store.save()    # save store record

            messages.success(request, f'Store "{new_store.name}" has been successfully registered!')
            return redirect('add_new_store')
        
        elif store_location_form.is_valid():
            store_location_form.save()

            messages.success(request, 'Location and time details have been successfully saved!')
            return redirect('add_new_store')
        
        elif store_contact_form.is_valid():
            store_contact_form.save()

            messages.success(request, 'Contact info successfully saved!')
            return redirect('dashboard', request.user)
        
    try:
        store_obj = RetailStore.objects.get(owner=request.user)
    except RetailStore.DoesNotExist:
        store_obj = None

    context = {
        'RetailStoreInfoForm': store_info_form, 'RetailStoreLocationForm': store_location_form, 'RetailStoreContactForm': store_contact_form,
        'store_obj': store_obj,
        }
    return render(request, 'dashboard/stores.html', context)


@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_shopowner is True and user.is_staff is False and  user.is_superuser is False)
def add_stocks_view(request, retail_store):
    store_obj = RetailStore.objects.get(store=retail_store)
    form = AddNewStockForm(instance=store_obj)

    if request.method == 'POST':
        form = AddNewStockForm(request.POST, request.FILES, instance=store_obj)

        if form.is_valid():
            new_stock = form.save(commit=False)
            new_stock.cost = new_stock.price * new_stock.quantity   # calculate cost of the item -> cost = price * quantity
            new_stock.save()

            messages.success(request, 'Item has been added successfully!')
            return redirect('')


    context = {'AddStockItemForm': form}
    return render(request, 'stores/stock.html', context)


# view to handle CRUD - Update

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_shopowner is True and user.is_staff is False and  user.is_superuser is False)
def edit_retailstore_view(request, store):
    store_obj = RetailStore.objects.get(id=store)
    edit_store_info_form = RetailStoreInfoForm(instance=store_obj)
    edit_store_location_form = RetailStoreLocationForm(instance=store_obj)
    edit_store_contact_form = RetailStoreContactsandSocialLinksForm(instance=store_obj)

    if request.method == 'POST':
        edit_store_info_form = RetailStoreInfoForm(request.POST, request.FILES, instance=store_obj)
        edit_store_location_form = RetailStoreLocationForm(request.POST, instance=store_obj)
        edit_store_contact_form = RetailStoreContactsandSocialLinksForm(request.POST, instance=store_obj)

        if edit_store_info_form.is_valid():
            edit_store_info_form.save()

            messages.info(request, f'Store details has been successfully updated!')
            return redirect('add_new_store')
        
        elif edit_store_location_form.is_valid():
            edit_store_location_form.save()

            messages.info(request, 'Details have been successfully saved!')
            return redirect('add_new_store')
        
        elif edit_store_contact_form.is_valid():
            edit_store_contact_form.save()

            messages.info(request, 'Contact info. updated successfully!')
            return redirect('add_new_store')
        
    context = {
        'EditStoreDetailsForm': edit_store_info_form, 'EditStoreLocationForm': edit_store_location_form,
        'EditStoreContactForm': edit_store_contact_form, 
        'url_obj': store,  # ref. to 
        }
    return render(request, 'dashboard/store-info.html', context)

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_shopowner is True and user.is_staff is False and  user.is_superuser is False)
def edit_stockitem_view(request, id):
    stock_obj = Stock.objects.get(id=id)
    form = EditStockItemForm(instance=stock_obj)

    if request.method == 'POST':
        form = EditStockItemForm(request.POST, request.FILES, instance=stock_obj)
        if form.is_valid():
            update_stock = form.save(commit=False)
            update_stock.cost = update_stock.price * update_stock.quantity
            update_stock.save()

            messages.warning(request, 'Stock item updated successfully!')
            return redirect('edit_stock_info', id)

    context = {'EditStockInfo': form}
    return render(request, 'stores/', context)

