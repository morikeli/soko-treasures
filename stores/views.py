from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import CreateRetailStoreForm, AddProductForm, EditStoreInfoForm, EditProductInfoForm, PlaceOrderForm
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
    
class ProductsListView(View):
    template_name = 'stores/products.html'

    def get(self, request, store_id, *args, **kwargs):
        store_obj = RetailStores.objects.get(id=store_id)
        products_list = Products.objects.filter(seller_id=store_obj.id).all().order_by('product')
        similar_products = Products.objects.filter(seller__services=store_obj.services).all().order_by('product', '-created')

        context = {
            'products_on_sale': products_list, 
            'similar_products': similar_products,
            'store_obj': store_obj,
        }
        return render(request, self.template_name, context)
    
class AllProductsListView(View):
    template_name = 'stores/all-items.html'

    def get(self, request, *args, **kwargs):
        items = Products.objects.filter(out_of_stock=False).all().order_by('product')

        if request.method == 'GET':
            item_category = request.GET.get('item-category')
            search_item = request.GET.get('search-item')

            if item_category is None and search_item is None:
                items   # if None is returned, use the default QS -> items
            else:
                if item_category != '' and search_item != '':   # if the two inputs are not blank, search for exisiting QS.
                    items = Products.objects.filter(product__icontains=search_item, seller__services=item_category).all().order_by('product')
                elif item_category != '':
                    items = Products.objects.filter(seller__services=item_category).all().order_by('product')
                elif search_item != '':
                    items = Products.objects.filter(product__icontains=search_item).all().order_by('product')
                else:
                    messages.error(request, 'Item not found!')
                    return items

        context = {
            'items_for_sale': items,

        }
        return render(request, self.template_name, context)
    
class CustomerOrdersView(View):
    form_class = PlaceOrderForm
    template_name = 'stores/order.html'

    def get(self, request, product_id, *args, **kwargs):
        product_obj = Products.objects.get(id=product_id)
        placed_order_info = {
            'item': product_obj.product,
            'price': product_obj.price,
            'quantity': 0,
            
        }
        form = self.form_class(instance=product_obj, initial=placed_order_info)


        context = {
            'PlaceOrderForm': form,
            'product_obj': product_obj,

        }
        return render(request, self.template_name, context)
    
    def post(self, request, product_id, *args, **kwargs):
        product_obj = Products.objects.get(id=product_id)
        form = self.form_class(instance=product_obj)

        context = {'PlaceOrderForm': form}
        return render(request, self.template_name, context)
    
    

# Dashboard views

@method_decorator(login_required(login_url='login'), name='get')
class DashboardView(View):
    template_name = 'dashboard/homepage.html'

    def get(self, request, store_id, *args, **kwargs):
        store_obj = RetailStores.objects.get(id=store_id)
        total_products = Products.objects.filter(seller_id=store_id).all().count()

        context = {
            'store_obj': store_obj,
            'TotalProducts': total_products,
        }
        return render(request, self.template_name, context)

@method_decorator(login_required(login_url='login'), name='get')
class RetailStoresRegistrationView(View):
    form_class = CreateRetailStoreForm
    template_name = 'dashboard/create-store.html'

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
    template_name = 'dashboard/products.html'

    def get(self, request, store_id, *args, **kwargs):
        form = self.form_class()
        store_obj = RetailStores.objects.get(id=store_id)
        stock_items = Products.objects.filter(seller_id=store_id).all().order_by('-created', 'product')    # items on sale (i.e. current stock)

        context = {
            'NewProductsForm': form,
            'items_in_stock': stock_items,
            'store_obj': store_obj,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, store_id, *args, **kwargs):
        store_obj = RetailStores.objects.get(id=store_id)
        form = self.form_class(request.POST, request.FILES)
        
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.seller = store_obj
            new_product.save()
            messages.info(request, 'Product has been added successfully!')
            return redirect('add_product', store_id)
        
        context = {
            'NewProductsForm': form,
            'store_obj': store_obj,
        }
        return render(request, self.template_name, context)

# CRUD views
@method_decorator(login_required(login_url='login'), name='get')
class UpdateRetailStoreInfoView(View):
    form_class = EditStoreInfoForm
    template_name = 'dashboard/store-info.html'

    def get(self, request, store_id, *args, **kwargs):
        store_obj = RetailStores.objects.get(id=store_id)
        form = self.form_class(instance=store_obj)

        context = {'EditStoreInfoForm': form, 'store_obj': store_obj}
        return render(request, self.template_name, context)
    
    def post(self, request, store_id, *args, **kwargs):
        store_obj = RetailStores.objects.get(id=store_id)
        form = self.form_class(request.POST, request.FILES, instance=store_obj)
        
        if form.is_valid():
            form.save()
            messages.warning(request, 'You have updated your retail store info!')
            return redirect('edit_store', store_id)

@method_decorator(login_required(login_url='login'), name='get')
class EditProductsView(View):
    form_class = EditProductInfoForm
    template_name = 'dashboard/edit-products.html'

    def get(self, request, product_id, *args, **kwargs):
        product_obj = Products.objects.get(id=product_id)
        store_obj = RetailStores.objects.get(id=product_obj.seller_id)
        form = self.form_class(instance=product_obj)

        context = {
            'EditProductsForm': form,
            'store_obj': store_obj,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, product_id, *args, **kwargs):
        product_obj = Products.objects.get(id=product_id)
        store_obj = RetailStores.objects.get(id=product_obj.seller_id)
        form = self.form_class(request.POST, request.FILES, instance=product_obj)

        if form.is_valid():
            form.save()
            messages.info(request, 'Product info. updated successfully!')
            return redirect('add_product', store_obj.id)
        
        context = {'EditProductsForm': form}
        return render(request, self.template_name, context)
