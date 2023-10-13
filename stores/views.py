from .forms import (CreateRetailStoreForm, AddProductForm, EditStoreInfoForm, EditProductInfoForm, RateRetailStoreForm, RateProductsForm, 
    ReportRetailStoreForm, CustomerOrderForm, )
from .models import RetailStores, Products, CartItems, Cart, Polls, ShippingDetails
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
from django.db.models import Sum
from uuid import uuid4

class HomepageView(View):
    template_name = 'stores/index.html'

    def get(self, request, *args, **kwargs):
        stores = RetailStores.objects.all().order_by('name')

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

class ProductDetailView(View):
    template_name = 'stores/product-info.html'

    def get(self, request, product_id, *args, **kwargs):
        product_obj = Products.objects.get(id=product_id)
        session = str(request.META.get('HTTP_COOKIE')).removeprefix('csrftoken=')
        cart_items = CartItems.objects.filter(order__session_id=session).all()
        sum_of_cartitems = cart_items.aggregate(quantity=Sum('quantity'))["quantity"]
        total_cost_items = 0
        cost_list = []

        for item in cart_items:
            total_cost_items = item.quantity * item.product.price
            cost_list.append(total_cost_items)
            
        total_cost_items = sum([cost for cost in cost_list])

        context = {
            'product_obj': product_obj,
            'cart': cart_items,
            'SumofCartItems': sum_of_cartitems,
            'TotalCost': total_cost_items,
        }
        return render(request, self.template_name, context)

    def post(self, request, product_id, *args, **kwargs):
        item_id = request.POST.get('item-id')
        product_obj = Products.objects.get(id=item_id)

        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(customer=request.user, completed=False)
            cartitem, created = CartItems.objects.get_or_create(product=product_obj, order=cart)
            cartitem.quantity += 1
            cartitem.save()
            total_cart_items = cart.get_cart_items

        else:
            session = str(request.META.get('HTTP_COOKIE')).removeprefix('csrftoken=')
            cart, created = Cart.objects.get_or_create(session_id=session, completed=False)        
            cartitem, created = CartItems.objects.get_or_create(product=product_obj, order=cart)
            cartitem.quantity += 1
            cartitem.save()
            total_cart_items = cart.get_cart_items

            return redirect('add_to_cart', product_id)
        
        context = {'product_obj': product_obj, 'cart': cart}
        return render(request, self.template_name, context)

class ProductsListView(View):
    template_name = 'stores/products.html'

    def get(self, request, store_id, *args, **kwargs):
        store_obj = RetailStores.objects.get(id=store_id)
        products_list = Products.objects.filter(seller_id=store_obj.id).all().order_by('product')
        similar_products = Products.objects.filter(seller__services=store_obj.services).all().order_by('product', '-created').exclude(seller_id=store_id)

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

        # search queryset for an item and/or category of the item.
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
                return redirect('all_products')

        context = {
            'items_for_sale': items,

        }
        return render(request, self.template_name, context)
    
class ItemsinCartView(View):
    template_name = 'stores/cart.html'

    def get(self, request, *args, **kwargs):
        item_id = request.GET.get('cart-item')
        minusitem_id = request.GET.get('minus-cart-item')
        deleteitem_id = request.GET.get('delete-cart-item')

        session = str(request.META.get('HTTP_COOKIE')).removeprefix('csrftoken=')
        cart_items = CartItems.objects.filter(order__session_id=session).all()
        total_cart_items = cart_items.count()
        total_cost_items = 0

        try:
            if not item_id is None:
                update_cart = CartItems.objects.get(id=item_id)
                update_cart.quantity += 1
                update_cart.save()

                item_cost = [item.quantity * item.product.price for item in cart_items]   # calculate item of each item.
                total_cost_items = sum(item.quantity * item.product.price for item in cart_items)
                data = {
                    "quantity": update_cart.quantity,
                    'total_cost': total_cost_items,
                    'item_cost': item_cost,
                }
                return JsonResponse(data)
            
            elif minusitem_id is not None:
                update_cart = CartItems.objects.get(id=minusitem_id)
                update_cart.quantity -= 1
                update_cart.save()

                item_cost = [item.quantity * item.product.price for item in cart_items]   # calculate item of each item.
                total_cost_items = sum(item.quantity * item.product.price for item in cart_items)
                data = {
                    "quantity": update_cart.quantity,
                    'total_cost': total_cost_items,
                    'item_cost': item_cost,
                }
                return JsonResponse(data)
            
            elif deleteitem_id is not None:
                update_cart = CartItems.objects.get(id=deleteitem_id)
                update_cart.delete()

                item_cost = [item.quantity * item.product.price for item in cart_items]   # calculate item of each item.
                total_cost_items = sum(item.quantity * item.product.price for item in cart_items)
                data = {
                    "quantity": update_cart.quantity,
                    'total_cost': total_cost_items,
                    'item_cost': item_cost,
                }
                return JsonResponse(data)
            

        except CartItems.DoesNotExist:
            pass
        
        total_cost_items = sum(item.quantity * item.product.price for item in cart_items)
        item_cost = [item.quantity * item.product.price for item in cart_items]
        context = {
            'cart': cart_items,
            'TotalCartItems': total_cart_items,
            'TotalCost': total_cost_items,
            'CostofItem': item_cost,
        }
        return render(request, self.template_name, context)

class CartCheckoutView(View):
    form_class = CustomerOrderForm
    template_name = 'stores/checkout.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        session = str(request.META.get('HTTP_COOKIE')).removeprefix('csrftoken=')
        cart_items = CartItems.objects.filter(order__session_id=session).all()
        total_cart_items = cart_items.count()
        total_cost_items = sum(item.quantity * item.product.price for item in cart_items)
        sum_of_cartitems = cart_items.aggregate(quantity=Sum('quantity'))["quantity"]
        
        context = {
            'CheckoutForm': form,
            'cart': cart_items,
            'TotalCartItems': total_cart_items,
            'TotalCost': total_cost_items,
            'SumofCartItems': sum_of_cartitems,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        session = str(request.META.get('HTTP_COOKIE')).removeprefix('csrftoken=')
        cart_items = CartItems.objects.filter(order__session_id=session).all()
        total_cart_items = cart_items.count()
        total_cost_items = sum(item.quantity * item.product.price for item in cart_items)
        sum_of_cartitems = cart_items.aggregate(quantity=Sum('quantity'))["quantity"]

        if form.is_valid():
            placeorder = form.save(commit=False)
            
            # iterate user's cart to get all items in cart
            for item in cart_items:
                cartitems_obj = CartItems.objects.get(id=item.id)   # fetch item ID and create an object.

                # save user orders using the form and the created object.
                get_order = ShippingDetails.objects.create(
                    order=cartitems_obj,
                    name=placeorder.name,
                    mobile_no=placeorder.mobile_no,
                    email=placeorder.email,
                    country=placeorder.country,
                    county=placeorder.county,
                    city=placeorder.city,
                    address=placeorder.address,
                ).save()
            
            messages.success(request, 'You order has been successfully submitted!')
            return redirect('checkout')
        
        context = {
            'CheckoutForm': form,
            'cart': cart_items,
            'TotalCartItems': total_cart_items,
            'TotalCost': total_cost_items,
            'SumofCartItems': sum_of_cartitems,
        }
        return render(request, self.template_name, context)


class RateRetailStoresView(View):
    form_class = RateRetailStoreForm
    template_name = 'stores/rate-stores.html'

    def get(self, request, store_id, *args, **kwargs):
        store_obj = RetailStores.objects.get(id=store_id)
        form = self.form_class()

        context = {
            'RateRetailStoreForm': form,
            'store_obj': store_obj,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, store_id, *args, **kwargs):
        store_obj = RetailStores.objects.get(id=store_id)
        form = self.form_class(request.POST, instance=store_obj)

        if form.is_valid():
            votes = form.save(commit=False)
            votes.total_votes += 1
            votes.save()

            if request.user.is_authenticated:
                rate_store, created = Polls.objects.get_or_create(voter=request.user, store=store_obj, product=None)
            else:
                rate_store, created = Polls.objects.get_or_create(store=store_obj, product=None)

            messages.info(request, 'Thank you for your feedback!')
            return redirect('retail_store', store_id)

        context = {'RateRetailStoreForm': form, 'store_obj': store_obj}
        return render(request, self.template_name, context)

class RateProductsView(View):
    form_class = RateProductsForm
    template_name = 'stores/rate-products.html'

    def get(self, request, product_id, *args, **kwargs):
        product_obj = Products.objects.get(id=product_id)
        form = self.form_class()

        context = {
            'RateProductsForm': form,
            'product_obj': product_obj,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, product_id, *args, **kwargs):
        product_obj = Products.objects.get(id=product_id)
        form = self.form_class(request.POST, instance=product_obj)
        if form.is_valid():
            votes = form.save(commit=False)
            votes.total_votes += 1
            votes.save()

            if request.user.is_authenticated:
                rate_store, created = Polls.objects.get_or_create(voter=request.user, store=product_obj.seller, product=product_obj)
            else:
                rate_store, created = Polls.objects.get_or_create(voter=None, store=product_obj.seller, product=product_obj)

            messages.success(request, 'Your rating was successfully submitted!')
            return redirect('all_products')

        context = {'RateProductsForm': form, 'store_obj': product_obj}
        return render(request, self.template_name, context)

class ReportRetailStoresView(View):
    form_class = ReportRetailStoreForm
    template_name = 'stores/report-store.html'

    def get(self, request, store_id, *args, **kwargs):
        store_obj = RetailStores.objects.get(id=store_id)
        form = self.form_class()

        context = {'ReportRetailStoreForm': form, 'store_obj': store_obj}
        return render(request, self.template_name, context)

    def post(self, request, store_id, *args, **kwargs):
        store_obj = RetailStores.objects.get(id=store_id)
        form = self.form_class(request.POST)

        if form.is_valid():
            report_store = form.save(commit=False)
            report_store.store = store_obj
            report_store.save()

            messages.success(request, 'Report submitted successfully! We will review your report.')
            return redirect('retail_store', store_id)

        context = {'ReportRetailStoreForm': form, 'store_obj': store_obj}
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
