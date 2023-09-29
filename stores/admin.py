from .models import RetailStores, Products
from django.contrib import admin


@admin.register(RetailStores)
class RetailStoreTable(admin.ModelAdmin):
    list_display = ['owner', 'name', 'services', 'rating', 'created']
    readonly_fields = ['owner', 'name', 'description', 'services', 'rating', 'fb_url', 'x_url', 'ig_url', 'image', 'cover_photo']

@admin.register(Products)
class ProductsTable(admin.ModelAdmin):
    list_display = ['seller', 'product', 'quantity', 'price', 'cost', 'out_of_stock']
    readonly_fields = ['seller', 'product', 'description', 'quantity', 'price', 'cost', 'out_of_stock', 'img_file']