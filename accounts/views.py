from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import SignupForm, EditProfileForm


class UserLoginView(LoginView):
    """ This view handles login requests, user authentication and validation. """
    template_name = 'accounts/login.html'

class SignupView(View):
    """ This view enables a user to create new account. """
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {'SignupForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('login')
        
        return render(request, self.template_name)
    
@method_decorator(login_required(login_url='login'), name='get')
class UserProfileView(View):
    """ This view enables a user to update/edit his/her profile. """
    form_class = EditProfileForm
    template_name = 'accounts/profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {'EditProfileForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            messages.info(request, 'You have edited your profile!')
            return redirect('user_profile')
        
        return render(request, self.template_name)

class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'
