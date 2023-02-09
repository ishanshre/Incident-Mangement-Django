from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        return self.username

class GENDER_CHOICES(models.TextChoices):
    MALE = "M",'Male'
    FEMALE = "F",'Female'
    OTHER = "O",'Others'


class Role(models.Model):
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="user/profile", default="profile/avatar.jpeg")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES.choices, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_leader = models.BooleanField(default=False)
    phone_number = PhoneNumberField(null=True, blank=True)
    role = models.ManyToManyField(Role, blank=True)


    def __str__(self):
        return f"{self.user.username.title()}'s Profile"


