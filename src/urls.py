from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('', include('stores.urls')),
    path('auth/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^files/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
