from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.views import View
from .forms import SignupForm, UpdateProfileForm
from .models import User

class UsersLoginView(View):
    def get(self, request):
        form = AuthenticationForm()

        context = {'LoginForm': form}
        return render(request, 'accounts/login.html', context)
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user_account = auth.authenticate(username=username, password=password)
            
            if user_account is not None:
                pass


class SignupView(View):
    def get(self, request):
        form = SignupForm()

        context = {'SignupForm': form}
        return render(request, 'acounts/signup.html', context)
    
    def post(self, request):
        form = SignupForm()

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            
            messages.success(request, 'User account successfully created!')
            return redirect('profile', new_user.username)


class UpdateProfileView(View):
    def get(self, request, user):
        user_obj = User.objects.get(username=user)
        form = UpdateProfileForm(instance=user_obj)

        context = {'UpdateProfileForm': form}
        return render(request, 'accounts/profile.html', context)
    
    def post(self, request, user):
        user_obj = User.objects.get(username=user)
        form = UpdateProfileForm(instance=user_obj)

        if form.is_valid():
            form.save()

            messages.success(request, 'Profile successfully updated!')
            return redirect('profile', user)
        

class LogoutUsersView(LogoutView):
    template_name = 'accounts/logout.html'