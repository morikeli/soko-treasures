from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm, EditProfileForm
from .models import User
from stores.models import RetailStore

def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user_account = authenticate(email=username, password=password)

            if user_account is not None:
                if user_account.is_shopowner is False:
                    login(request, user_account)
                
                else:
                    try:
                        store = RetailStore.objects.get(owner=user_account)
                        if user_account.is_shopowner is True and store is not None:
                            login(request, user_account)
                            return redirect('dashboard', user_account.username)     # return the user to the retailstore dashboard
                    
                    except RetailStore.DoesNotExist:
                        login(request, user_account)
                        return redirect('add_new_store')
                    

    context = {'LoginForm': form}
    return render(request, 'accounts/login.html', context)

def signup_view(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_customer = True
            new_user.save()

            messages.success(request, 'Account created successfully!')
            return redirect('user_login')

    context = {'SignupForm': form}
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

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_shopowner is True and user.is_staff is False and user.is_superuser is False)
def update_staff_profile_view(request, staff_name):
    """ This view enables staff members of a retail store to update their profile. """
    staff = User.objects.get(username=staff_name)

    form = EditProfileForm(instance=staff)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=staff)

        if form.is_valid():
            form.save()

            messages.success(request, 'You have successfully your profile!')
            return redirect('staff_profile', staff_name)

    context = {'EditProfileForm': form}
    return render(request, 'dashboard/profile.html', context)

class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'

