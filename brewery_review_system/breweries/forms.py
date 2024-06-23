from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Review

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }