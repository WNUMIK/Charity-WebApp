from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from .models import Donation


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Hasło"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Powtórz hasło"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))

    class Meta:
        model = get_user_model()
        fields = ('name', 'surname', 'email', 'password')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError('Passwords don`t match')

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.TextInput(attrs={
        'type': 'text',
        'email': 'username',
        'placeholder': 'Email'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))

    class Meta:
        fields = ('username', 'password')


