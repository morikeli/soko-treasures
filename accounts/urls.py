from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('logout/', views.LogoutUser.as_view(), name='logout_user'),
]