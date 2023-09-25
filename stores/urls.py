from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/store/', views.RetailStoresRegistrationView.as_view(), name='register_store'),
    path('<str:store>/new/product/', views.NewProductsView.as_view(), name='add_product'),
    
]