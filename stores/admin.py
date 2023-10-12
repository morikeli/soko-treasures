from .models import RetailStores, Products, Cart, CartItems, Reports, Polls, ShippingDetails
from django.contrib import admin


@admin.register(RetailStores)
class RetailStoreTable(admin.ModelAdmin):
    list_display = ['owner', 'name', 'services', 'rating', 'created']
    readonly_fields = ['owner', 'name', 'description', 'services', 'address', 'rating', 'total_votes', 'fb_url', 'x_url', 'ig_url', 'image', 'cover_photo']

@admin.register(Products)
class ProductsTable(admin.ModelAdmin):
    list_display = ['seller', 'product', 'quantity', 'price', 'cost', 'out_of_stock']
    readonly_fields = ['seller', 'product', 'description', 'rating', 'total_votes', 'quantity', 'price', 'cost', 'out_of_stock', 'img_file']

@admin.register(Cart)
class UsersCartTable(admin.ModelAdmin):
    list_display = ['session_id', 'date_ordered', 'completed']
    readonly_fields = ['session_id']

@admin.register(CartItems)
class UsersCartItemsTable(admin.ModelAdmin):
    list_display = ['product', 'order', 'quantity']
    readonly_fields = ['product', 'order', 'quantity']

@admin.register(Reports)
class ReportedRetailStoresIssuesTable(admin.ModelAdmin):
    list_display = ['store', 'crime', 'date_reported']
    readonly_fields = ['store', 'feedback', 'crime']

@admin.register(Polls)
class UserPollsTable(admin.ModelAdmin):
    list_display = ['store', 'product', 'voting_date']
    readonly_fields = ['voter', 'store', 'product']

@admin.register(ShippingDetails)
class ShippingDetailsTable(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'county', 'date_ordered']
    readonly_fields = ['name', 'email', 'mobile_no', 'country', 'county', 'city', 'address']