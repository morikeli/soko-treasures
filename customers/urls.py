from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('store/<str:retail_store>/details/', views.store_details_view, name='retail_store_info'),   
]