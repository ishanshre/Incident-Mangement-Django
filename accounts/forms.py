from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from django.core.exceptions import ValidationError

from django import forms


from datetime import date

from accounts.models import Profile

from phonenumber_field.widgets import PhoneNumberPrefixWidget

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields =['username','email']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)

    class Meta: 
        model = User
        fields = ['username','password','remember_me']


class UserForm(forms.ModelForm):
    class Meta:
        model =  User
        fields = ['first_name','last_name','username','email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio','gender','date_of_birth','phone_number','role','is_leader']
        widgets = {
            "phone_number": PhoneNumberPrefixWidget(initial="NP"),
        }
    
    def clean_date_of_birth(self, *args, **kwargs):
        dateOfBirth = self.cleaned_data.get("date_of_birth")
        if dateOfBirth is not None:
            if dateOfBirth > date.today():
                raise ValidationError("Invalid Date of Birth")
        return dateOfBirth