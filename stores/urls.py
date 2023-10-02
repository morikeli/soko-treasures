from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.HomepageView.as_view(), name='index'),
    path('item/<str:product_id>/order/', views.CustomerOrdersView.as_view(), name='order_item'),
    path('create/<str:username>/store/', views.RetailStoresRegistrationView.as_view(), name='register_store'),
    path('store/<str:store_id>/dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('store/<str:retailstore>/info/', views.RetailStoreInfoView.as_view(), name='retail_store'),
    path('store/<str:store_id>/products/', views.ProductsListView.as_view(), name='products_for_sale'),
    path('store/<str:store_id>/edit/', views.UpdateRetailStoreInfoView.as_view(), name='edit_store'),
    path('product/<str:store_id>/new/', views.NewProductsView.as_view(), name='add_product'),
    path('product/<str:product_id>/edit/', views.EditProductsView.as_view(), name='edit_product'),
]