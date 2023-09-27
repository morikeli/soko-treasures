from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import CreateRetailStoreForm, AddProductForm, EditStoreInfoForm, EditProductInfoForm
from .models import RetailStores, Products


class HomepageView(View):
    template_name = 'stores/index.html'

    def get(self, request, *args, **kwargs):
        stores = RetailStores.objects.all()
        
        context = {
            'retail_stores': stores,
        }
        return render(request, self.template_name, context)

class RetailStoreInfoView(View):
    template_name = 'stores/stores.html'

    def get(self, request, retailstore, *args, **kwargs):
        store_info = RetailStores.objects.get(id=retailstore)
        products = Products.objects.filter(seller_id=retailstore, out_of_stock=False)  # products for sale

        context = {
            'store_info': store_info,
            'products': products,
        }
        return render(request, self.template_name, context)

# Dashboard views

@method_decorator(login_required(login_url='login'), name='get')
class RetailStoresRegistrationView(View):
    form_class = CreateRetailStoreForm
    template_name = ''

    def get(self, request, username, *args, **kwargs):
        form = self.form_class()
        context = {'StoreRegistrationForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, username, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Retail store successfully registered!')
            return redirect('register_store', username)
        
        return render(request, self.template_name)


@method_decorator(login_required(login_url='login'), name='get')
class NewProductsView(View):
    form_class = AddProductForm
    template_name = ''

    def get(self, request, store, *args, **kwargs):
        form = self.form_class()
        context = {'NewProductsForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, store, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            messages.info(request, 'Product has been added successfully!')
            return redirect('add_product', store)

# CRUD views

@method_decorator(login_required(login_url='login'), name='get')
class UpdateRetailStoreInfo(View):
    form_class = EditStoreInfoForm
    template_name = ''

    def get(self, request, store, *args, **kwargs):
        form = self.form_class(instance=store)
        context = {'EditStoreInfoForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, store, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=store)
        
        if form.is_valid():
            form.save()
            messages.warning(request, 'You have updated your retail store info!')
            return redirect('edit_store', store)

@method_decorator(login_required(login_url='login'), name='get')
class EditProductsView(View):
    form_class = EditProductInfoForm
    template_name = ''

    def get(self, request, id, *args, **kwargs):
        form = self.form_class(instance=id)
        context = {'EditProductsForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, id, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=id)

        if form.is_valid():
            form.save()
            messages.info(request, 'Product info. updated successfully!')
            return redirect('edit_product', id)
