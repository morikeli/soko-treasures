from django.contrib import admin
from .models import RetailStores, Branches, Employees


@admin.register(RetailStores)
class RetailStoresTable(admin.ModelAdmin):
    list_display = ['store', 'name', 'location']
    readonly_fields = [
        'store', 'mobile_no_1', 'mobile_no_2', ' location', 'address', 'service', 'opening_hours', 
        'closing_hours', 'working_days', 'facebook_url', 'twitter_url', 'image',
        ]

@admin.register(Branches)
class BranchesTable(admin.ModelAdmin):
    list_display = ['name', 'branch', 'location', 'address']
    readonly_fields = ['name', 'location', 'address', 'image']

@admin.register(Employees)
class EmployeesInfoTable(admin.ModelAdmin):
    list_display = ['full_name', 'gender', 'retail_store', 'branch', 'role']
    readonly_fields = ['full_name', 'branch', 'gender', 'phone_no', 'email', 'role', 'salary', 'image']

