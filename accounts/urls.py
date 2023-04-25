from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('<str:user>/profile', views.UpdateProfileView, name='profile'),
    path('logout/', views.LogoutUsersView.as_view(), name='logout_user'),

]