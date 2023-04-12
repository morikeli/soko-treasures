from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('customers.urls')),
    path('auth/', include('accounts.urls')),
    path('stores/', include('stores.urls')),
    path('admin/', admin.site.urls),
]
