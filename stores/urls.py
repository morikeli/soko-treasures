from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/business/<str:staff>/homepage', views.DashboardHomepageView.as_view(), name='dashboard'),
    path('dashboard/business/store-registration/', views.RetailStoresRegistrationView.as_view(), name='registration'),
    path('dashboard/business/<str:store>/branches/', views.RegisterBranchStoreView.as_view(), name='add_branch'),
    path('dashboard/business/<str:store>/employees/', views.AddNewEmployeeView.as_view(), name='add_employee'),
    path('dashboard/business/<str:store>/products/', views.AddNewProductsView.as_view(), name='products'),

]