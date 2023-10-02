from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.conf import settings
from .forms import UserLoginForm, SignupForm, EditProfileForm
from stores.forms import CreateRetailStoreForm
from stores.models import RetailStores
from formtools.wizard.views import SessionWizardView
import os

class UserLoginView(View):
    """ This view handles login requests, user authentication and validation. """
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {'LoginForm': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            store_name = form.cleaned_data['store_name']
            password = form.cleaned_data['password']
            
            user_acc = authenticate(username=username, password=password)

            if user_acc is None:
                messages.error(request, 'Invalid credentials! Please try again.')
                return redirect('login')
            
            else:
                try:
                    store_info = RetailStores.objects.get(name=store_name)
                    if store_info:
                        login(request, user_acc)
                        return redirect('dashboard', store_info.id)
                    
                except RetailStores.DoesNotExist:
                    messages.error(request, 'Invalid credentials! Please try again.')
                    return redirect('login')

        context = {'LoginForm': form}
        return render(request, self.template_name, context)

class SignupView(SessionWizardView):
    """ This view enables a user to create new account. """
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'media'))
    form_list = [SignupForm, CreateRetailStoreForm]
    template_name = 'accounts/signup.html'

    def done(self, form_list, **kwargs):
        registration_form = form_list[1]
        new_user = form_list[0].save(commit=False)
        
        if registration_form.is_valid():
            new_store = registration_form.save(commit=False)
            new_store.owner = new_user
            new_user.save()
            new_store.save()
            
            messages.success(self.request, 'Account successfully created!')
            return redirect('login')
    
@method_decorator(login_required(login_url='login'), name='get')
class UserProfileView(View):
    """ This view enables a user to update/edit his/her profile. """
    form_class = EditProfileForm
    template_name = 'accounts/profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)

        context = {'EditProfileForm': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            messages.info(request, 'You have edited your profile!')
            return redirect('user_profile')
        
        context = {'EditProfileForm': form}
        return render(request, self.template_name, context)

class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'
