from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from accounts.models import Profile, Role
# Register your models here.

User = get_user_model()

class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username','email','is_staff']
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (
            "Create User", {
                "classes":("wide",),
                "fields":('username','email','password1','password2'),
            }
        ),
    )
    def get_inlines(self, request, obj=None):
        if obj:
            return [ProfileInline]
        return []


admin.site.register(Role)