from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.HomepageView.as_view(), name='index'),
    path('info/<str:retailstore>/store/', views.RetailStoreInfoView.as_view(), name='retail_store'),
    path('create/<str:username>/store/', views.RetailStoresRegistrationView.as_view(), name='register_store'),
    path('<str:store>/new/product/', views.NewProductsView.as_view(), name='add_product'),
    path('store/<str:store>/edit/', views.UpdateRetailStoreInfo.as_view(), name='edit_store'),
    path('product/<str:id>/edit/', views.EditProductsView.as_view(), name='edit_product'),
]