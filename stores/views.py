from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StoreRegistrationForm, AddStockItemForm
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
def add_stocks_view(request, retail_store):
    store_obj = RetailStore.objects.get(store=retail_store)
    form = AddStockItemForm(instance=store_obj)

    if request.method == 'POST':
        form = AddStockItemForm(request.POST, request.FILES, instance=store_obj)

        if form.is_valid():
            form.save()

            messages.success(request, 'Item has been added successfully!')
            return redirect('')


    context = {'form': form}
    return render(request, 'stores/stock.html', context)