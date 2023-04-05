from django.urls import path
from . import views

urlpatterns = [
    path('new-store/', views.store_registration_view, name='add_new_store'),
    path('<str:retail_store>/add/new-stock/', views.add_stocks_view, name='add_new_stock'),
    path('<str:store>/edit-store-info/', views.edit_retailstore_view, name='edit_store_info'),
    path('<str:id>/edit-item-info/', views.edit_stockitem_view, name='edit_stock_info'),
    
]