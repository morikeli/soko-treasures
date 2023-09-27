from .models import RetailStores, Products
from django.contrib import admin


@admin.register(RetailStores)
class RetailStoreTable(admin.ModelAdmin):
    list_display = ['owner', 'name', 'services', 'rating', 'created']
    fields = ['owner', 'name', 'description', 'services', 'rating', 'fb_url', 'x_url', 'ig_url', 'image']

@admin.register(Products)
class ProductsTable(admin.ModelAdmin):
    list_display = ['seller', 'product', 'quantity', 'price', 'cost', 'out_of_stock']
    fields = ['seller', 'product', 'quantity', 'price', 'cost', 'out_of_stock', 'img_file']
