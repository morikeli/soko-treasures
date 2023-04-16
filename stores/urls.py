from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/new-store/', views.store_registration_view, name='add_new_store'),
    path('dashboard/staff/<str:staff_member>/homepage/', views.homepage_view, name='dashboard'),
    path('dashboard/<str:store>/branches/', views.retails_stores_branches_view, name='branches'),
    path('dashboard/<str:store>/employees/', views.employees_view, name='employees'),
    path('dashboard/<str:store>/products/', views.stock_records_view, name='add_products'),
    path('dashboard/<str:retail_store>/add/new-stock/', views.add_stocks_view, name='add_new_stock'),
    path('dashboard/<str:store>/edit-store-info/', views.edit_retailstore_view, name='edit_store_info'),
    path('dashboard/<str:id>/edit-item-info/', views.edit_stockitem_view, name='edit_stock_info'),
    
]