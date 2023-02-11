from django.urls import path

from django.contrib.auth.views import LogoutView
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('profile/', views.ProfileDetailAndUpdateView.as_view(), name="profile"),
    path('profile/<slug:username>/', views.ProfileView.as_view(), name="profile_view"),
]