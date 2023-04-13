from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='user_login'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('staff/<str:staff_name>/profile/', views.update_staff_profile_view, name='staff_profile'),
    path('logout/', views.LogoutUser.as_view(), name='logout_user'),
    
]