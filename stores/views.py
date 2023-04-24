from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import (
    RetailStoresInfoForm, RetailStoreContactandSocialsForm, RetailStoreLocationandAddressForm, AddEmployeesForm,
    BranchRegistrationForm, AddProductsForm, EditRetailStoresInfoForm, EditRetailStoreLocationandAddressForm,
    EditRetailStoreContactandSocialsForm, UpdateBranchDetailsForm, UpdateEmployeesProfileForm, UpdateProductsForm,
)
from .models import RetailStores, Branches, Employees, Products
from accounts.models import User


class DashboardHomepageView(View):
    """
        This is the homepage of the dashboard in business accounts.
    """
    def get(self, request, staff):
        user_obj = User.objects.get(username=staff)

        context = {}
        return render(request, 'dashboard/homepage.html', context)


class RetailStoresRegistrationView(View):
    def get(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        store_info_form = RetailStoresInfoForm()
        store_location_form = RetailStoreLocationandAddressForm()
        store_contact_form = RetailStoreContactandSocialsForm()

        context = {
            'RetailStoreInfoForm': store_info_form, 'RetailStoreLocationandAddressForm': store_location_form,
            'RetailStoreContactandSocialsForm': store_contact_form,
            
            }
        return render(request, 'dashboard/registration.html', context)


    def post(self, request, pk):
        store_info_form = RetailStoresInfoForm()

        try:
            store_obj = RetailStores.objects.get(id=pk)
            store_location_form = RetailStoreLocationandAddressForm(instance=store_obj)
            store_contact_form = RetailStoreContactandSocialsForm(instance=store_obj)
        
        except RetailStores.DoesNotExist:
            messages.error(request, 'Unknown error occured!')
            return redirect('registration', pk)

        if store_info_form.is_valid():
            new_store = store_info_form.save(commit=False)
            new_store.name = request.user
            new_store.save()

            messages.success(request, 'Retail store details successfully saved!')
            return redirect('registration', pk)

        elif store_location_form.is_valid():
            store_location_form.save()

            messages.success(request, 'Store info. successfully saved!')
            return redirect('registration', pk)

        elif store_contact_form.is_valid():
            store_contact_form.save()
            
            messages.success(request, 'Contact and social handles successfully saved!')
            return redirect('dashboard', request.user)


class RegisterBranchStoreView(View):
    def get(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        branch_reg_form = BranchRegistrationForm()

        context = {
            'BranchRegistrationForm': branch_reg_form,
        }
        return render(request, 'dashboard/', context)
    

    def post(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        branch_reg_form = BranchRegistrationForm()

        if branch_reg_form.is_valid():
            form = branch_reg_form.save(commit=False)
            form.branch = store
            form.save()

            messages.success(request, 'Branch details successfully saved!')
            return redirect('add_branch', pk)
        
class AddNewEmployeeView(View):
    def get(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        employees_form = AddEmployeesForm()

        context = {
            'AddNewEmployeeForm': employees_form,
            }
        return render(request, 'dashboard/employees.html', context)
    

    def post(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        employees_form = AddEmployeesForm()

        if employees_form.is_valid():
            form = employees_form.save(commit=False)
            form.retail_store = store
            form.save()

            messages.success(request, 'Employee successfully saved!')
            return redirect('add_employee', pk)

class AddNewProductsView(View):
    def get(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        product_form = AddProductsForm()

        context = {
            'AddProductsForm': product_form,
        }
        return render(request, 'dashboard/stock-management.html', context)
    

    def post(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        products_form = AddProductsForm()

        if products_form.is_valid():
            form = products_form.save(commit=False)
            form.seller = store
            form.cost = form.price * form.quantity  # calculate cost of the item
            form.save()

            messages.success(request, 'Item record successfully saved!')
            return redirect('products', pk)

# CRUD operations
class EditRetailStoreDetailsView(View):
    def get(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        store_info_form = EditRetailStoresInfoForm(instance=store)
        store_location_form = EditRetailStoreLocationandAddressForm(instance=store)
        store_contact_form = EditRetailStoreContactandSocialsForm(instance=store)

        context = {
            'RetailStoreInfoForm': store_info_form, 'RetailStoreLocationandAddressForm': store_location_form,
            'RetailStoreContactandSocialsForm': store_contact_form,
            
            }
        return render(request, 'dashboard/registration.html', context)

    def post(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        store_info_form = EditRetailStoresInfoForm(instance=store)
        store_location_form = EditRetailStoreLocationandAddressForm(instance=store)
        store_contact_form = EditRetailStoreContactandSocialsForm(instance=store)

        if store_info_form.is_valid():
            store_info_form.save()

            messages.info(request, 'Retail Store details successfully updated!')
            return redirect('registration', pk)
        
        elif store_location_form.is_valid():
            store_location_form.save()

            messages.info(request, 'Store info successfully updated!')
            return redirect('registration', pk)
        
        elif store_contact_form.is_valid():
            store_contact_form.save()
            
            messages.success(request, 'Contact and social handles successfully saved!')
            return redirect('dashboard', request.user)

class EditBranchStoreInfoView(View):
    def get(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        branch_reg_form = UpdateBranchDetailsForm(instance=store)

        context = {
            'BranchRegistrationForm': branch_reg_form,
        }
        return render(request, 'dashboard/', context)
    

    def post(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        branch_reg_form = UpdateBranchDetailsForm(instance=store)

        if branch_reg_form.is_valid():
            form = branch_reg_form.save(commit=False)
            form.branch = store
            form.save()

            messages.success(request, 'Branch details successfully saved!')
            return redirect('add_branch', pk)
        
class AddNewEmployeeView(View):
    def get(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        employees_form = UpdateEmployeesProfileForm(instance=store)

        context = {
            'AddNewEmployeeForm': employees_form,
            }
        return render(request, 'dashboard/employees.html', context)
    

    def post(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        employees_form = UpdateEmployeesProfileForm(instance=store)

        if employees_form.is_valid():
            form = employees_form.save(commit=False)
            form.retail_store = store
            form.save()

            messages.success(request, 'Employee successfully saved!')
            return redirect('add_employee', pk)

class AddNewProductsView(View):
    def get(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        product_form = UpdateProductsForm(instance=store)

        context = {
            'AddProductsForm': product_form,
        }
        return render(request, 'dashboard/stock-management.html', context)
    

    def post(self, request, pk):
        store = RetailStores.objects.get(id=pk)
        products_form = UpdateProductsForm(instance=store)

        if products_form.is_valid():
            form = products_form.save(commit=False)
            form.seller = store
            form.cost = form.price * form.quantity  # calculate cost of the item
            form.save()

            messages.success(request, 'Item record successfully saved!')
            return redirect('products', pk)

