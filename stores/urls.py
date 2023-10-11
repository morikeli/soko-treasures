from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.HomepageView.as_view(), name='index'),
    path('items/cart/', views.ItemsinCartView.as_view(), name='user_cart'),
    path('checkout/cart', views.CartCheckoutView.as_view(), name='checkout'),
    path('all-products/', views.AllProductsListView.as_view(), name='all_products'),
    path('item/<str:product_id>/product/', views.ProductDetailView.as_view(), name='add_to_cart'),
    path('create/<str:username>/store/', views.RetailStoresRegistrationView.as_view(), name='register_store'),
    path('store/<str:store_id>/dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('store/<str:retailstore>/info/', views.RetailStoreInfoView.as_view(), name='retail_store'),
    path('store/<str:store_id>/products/', views.ProductsListView.as_view(), name='products_for_sale'),
    path('store/<str:store_id>/edit/', views.UpdateRetailStoreInfoView.as_view(), name='edit_store'),
    path('store/<str:store_id>/rate/', views.RateRetailStoresView.as_view(), name='rate_store'),
    path('store/<str:store_id>/report/', views.ReportRetailStoresView.as_view(), name='report_store'),
    path('product/<str:store_id>/new/', views.NewProductsView.as_view(), name='add_product'),
    path('product/<str:product_id>/edit/', views.EditProductsView.as_view(), name='edit_product'),
    path('product/<str:product_id>/rate/', views.RateProductsView.as_view(), name='rate_product'),

]