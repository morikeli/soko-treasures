from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import CreateRetailStoreForm, AddProductForm

@method_decorator(login_required(login_url='login'), name='get')
class RetailStoresRegistrationView(View):
    form_class = CreateRetailStoreForm
    template_name = ''

    def get(self, request, username, *args, **kwargs):
        form = self.form_class()
        context = {'StoreRegistrationForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, username, *args, **kwargs):
        form = self.form_class(request.POST)

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