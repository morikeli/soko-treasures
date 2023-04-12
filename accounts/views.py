from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm, EditProfileForm


def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        # print(form.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user_account = authenticate(email=username, password=password)

            if user_account is not None:
                if user_account.is_shopowner is False:
                    login(request, user_account)
                
                else:
                    try:
                        if user_account.is_shopowner is True and user_account.retailstore.owner is not None:
                            login(request, user_account)
                            return redirect('index')
                    except:
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

class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'

