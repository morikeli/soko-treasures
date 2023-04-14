from django.contrib import admin
from .models import RetailStore, Stock, Transactions, Branches, Employees

@admin.register(RetailStore)
class RetailStoreTable(admin.ModelAdmin):
    list_display = ['owner', 'name', 'location', 'service']
    readonly_fields = ['name', 'description', 'mobile_no_1', 'mobile_no_2', 'location', 'address', 'service', 'opening_hours', 'closing_hours', 'working_days', 'facebook_url', 'instagram_url', 'linkedin_url']

@admin.register(Branches)
class RetailBranchesTable(admin.ModelAdmin):
    list_display = ['branch', 'location', 'address']
    readonly_fields = ['location', 'address', 'image']


@admin.register(Employees)
class RetailStoresEmployeesTable(admin.ModelAdmin):
    list_display = ['employee', 'store', 'salary', 'role']
    readonly_fields = ['employee', 'store', 'branch', 'salary', 'role']

@admin.register(Stock)
class StockTable(admin.ModelAdmin):
    list_display = ['store', 'item', 'cost', 'out_of_stock']
    readonly_fields = ['store', 'item', 'quantity', 'img', 'price', 'out_of_stock']

@admin.register(Transactions)
class TransactionsTable(admin.ModelAdmin):
    list_display = ['shop', 'customer', 'item', 'quantity', 'cost', 'payment']
    readonly_fields = ['shop', 'customer', 'item', 'quantity', 'price', 'cost', 'payment']
