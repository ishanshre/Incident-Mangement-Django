from django.shortcuts import render, redirect
from django.views.generic import CreateView


from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from accounts.forms import CustomUserCreationForm, UserLoginForm
# Create your views here.


class UserRegisterView(SuccessMessageMixin ,CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")
    success_message = "Account Successfully Created"
    
    def form_invalid(self, form):
        messages.error(self.request, "Error in Account Creation")
        return super().form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:index')
        return super(UserRegisterView, self).dispatch(request, *args, **kwargs)
   


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    success_message = "Login Successfull"
    success_url = reverse_lazy("core:index")
    def form_invalid(self, form):
        messages.error(self.request, "Error in Login")
        return super().form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:index')
        return super(UserLoginView,self).dispatch(request, *args, **kwargs)