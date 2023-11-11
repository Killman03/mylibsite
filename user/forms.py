from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control',  'placeholder': 'Почта'}))
    password1 = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',  'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control',  'placeholder': 'Подтвердить пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Пароли не совподают.')
    #     return cd['password2']
    #
    # def clean_email(self):
    #     data = self.cleaned_data['email']
    #     if User.objects.filter(email=data).exists():
    #         raise forms.ValidationError('Пользователь с такой почтой уже существует.')
    #     return data

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))