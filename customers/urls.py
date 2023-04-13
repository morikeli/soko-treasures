from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('store/<str:retail_store>/details/', views.store_details_view, name='retail_store_info'), 
    path('<str:retail_store>/products/', views.all_products_view, name='products'),
    path('products/<str:pk>/<str:item>/details/<str:retail_store>/', views.products_details_view, name='product_info')  
]