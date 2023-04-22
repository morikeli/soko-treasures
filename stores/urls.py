from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/business/<str:staff>/homepage/', views.DashboardHomepageView.as_view(), name='dashboard'),
    path('dashboard/business/<str:pk>/registration/', views.RetailStoresRegistrationView.as_view(), name='registration'),
    path('dashboard/business/<str:pk>/branches/', views.RegisterBranchStoreView.as_view(), name='add_branch'),
    path('dashboard/business/<str:pk>/employees/', views.AddNewEmployeesView.as_view(), name='add_employee'),
    path('dashboard/business/<str:pk>/products/', views.AddNewProductsView.as_view(), name='products'),
]