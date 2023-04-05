from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StoreRegistrationForm, AddNewStockForm, EditRetailStoreInfoForm, EditStockItemForm
from .models import RetailStore, Stock


@login_required(login_url='user_login')
def store_registration_view(request):
    form = StoreRegistrationForm()

    if request.method == 'POST':
        form = StoreRegistrationForm(request.POST)

        if form.is_valid():
            new_store = form.save(commit=False)
            new_store.owner = request.user
            new_store.save()

            messages.success(request, f'Store {new_store.name} has been registered successfully!')
            return redirect('')

    context = {'form': form}
    return render(request, 'stores/stores.html', context)


@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_shopowner is True and user.is_staff is False and  user.is_superuser is False)
def add_stocks_view(request, retail_store):
    store_obj = RetailStore.objects.get(store=retail_store)
    form = AddNewStockForm(instance=store_obj)

    if request.method == 'POST':
        form = AddNewStockForm(request.POST, request.FILES, instance=store_obj)

        if form.is_valid():
            form.save()

            messages.success(request, 'Item has been added successfully!')
            return redirect('')


    context = {'form': form}
    return render(request, 'stores/stock.html', context)


# view to handle CRUD - Update

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_shopowner is True and user.is_staff is False and  user.is_superuser is False)
def edit_retailstore_view(request, store):
    store_obj = RetailStore.objects.get(id=store)
    form = EditRetailStoreInfoForm(instance=store_obj)

    if request.method == 'POST':
        form = EditRetailStoreInfoForm(request.POST, request.FILES, instance=store_obj)

        if form.is_valid():
            form.save()
            messages.warning(request, 'You have updated your retail store details!')
            return redirect('edit_store_info', store)


    context = {'EditStoreDetailsForm': form}
    return render(request, 'stores/', context)

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_shopowner is True and user.is_staff is False and  user.is_superuser is False)
def edit_stockitem_view(request, id):
    stock_obj = Stock.objects.get(id=id)
    form = EditStockItemForm(instance=stock_obj)

    if request.method == 'POST':
        form = EditStockItemForm(request.POST, request.FILES, instance=stock_obj)
        if form.is_valid():
            form.save()

            messages.warning(request, 'Stock item updated successfully!')
            return redirect('edit_stock_info', id)

    context = {'EditStockInfo': form}
    return render(request, 'stores/', context)

