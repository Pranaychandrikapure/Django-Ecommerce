from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterFrom(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confrim your password'}))
    class Meta:
        model = User
        fields = ['username','email']