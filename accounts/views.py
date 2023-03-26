from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, EditProfileForm


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'


def signup_view(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_customer = True
            new_user.save()

            messages.success(request, 'Account created successfully!')
            return redirect('profile')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

@login_required(login_url='user_login')
def profile_view(request):
    form = EditProfileForm(instance=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            messages.info(request, 'Profile updated successfully!')
            return redirect('homepage')

    context = {'form': form}
    return render(request, 'accounts/profile.html', context)

class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'

