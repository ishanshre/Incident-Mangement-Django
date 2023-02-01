from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.views import View


from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from accounts.forms import CustomUserCreationForm, UserLoginForm, ProfileForm, CustomUserChangeForm
from accounts.models import Profile
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



class ProfileDetailAndUpdateView(LoginRequiredMixin, View):
    template_name = "accounts/profile.html"
    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user)
        profile_form = ProfileForm(instance=profile)
        user_form = CustomUserChangeForm(instance=request.user)
        context = {
            "profile":profile,
            "profile_form":profile_form,
            "user_form":user_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print(request.FILES)
        profile = get_object_or_404(Profile, user=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect("accounts:profile")
        context = {
            "profile":profile,
            "profile_form":profile_form,
            "user_form":user_form,
        }
        return render(request, self.template_name, context)
