from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('store/<str:retail_store>/details/', views.store_details_view, name='retail_store_info'), 
    path('<str:retail_store>/products/', views.all_products_view, name='products'),
    path('products/<str:pk>/details/', views.products_details_view, name='product_info'),
    path('<str:retail_store>/checkout/', views.checkout_view, name='checkout'),
]