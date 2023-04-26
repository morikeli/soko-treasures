from django_summernote.widgets import SummernoteWidget
from django.contrib import admin
from django.db import models
from .models import Products, Transactions, PaidOrders


@admin.register(Products)
class ProductsTable(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'price', 'out_of_stock']
    readonly_fields = ['name', 'description', 'quantity', 'price', 'image', 'out_of_stock']
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget}
    }


@admin.register(Transactions)
class TransactionsTable(admin.ModelAdmin):
    list_display = ['item', 'buyer', 'payment']
    readonly_fields = ['payment']


@admin.register(PaidOrders)
class PaidOrdersTable(admin.ModelAdmin):
    list_display = ['item', 'buyer']
    readonly_fields = ['payment']
