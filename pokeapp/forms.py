from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # unga custom user model

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'password1', 'password2']  # password1 & 2 for UserCreationForm
