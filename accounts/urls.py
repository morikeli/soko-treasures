from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UsersLoginView.as_view(), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('<str:user>/profile', views.UpdateProfileView.as_view(), name='profile'),
    path('logout/', views.LogoutUsersView.as_view(), name='logout_user'),

]