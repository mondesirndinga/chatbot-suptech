from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'age', 'current_class', 'formation', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nom d’utilisateur ou e-mail')
