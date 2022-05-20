import datetime

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import SelectDateWidget

from .models import IntebUser
from extras import *


class IntebUserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(label='Дата рождения', widget=SelectDateWidget(
        years=range(datetime.date.today().year - 15, 1920, -1),
        attrs={'class': 'form-control', })
    )
    avatar = forms.ImageField

    class Meta:
        model = IntebUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'middle_name', 'email', 'birthday',
                  'avatar']


class IntebUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control form-outline form-label mb-4'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control form-outline form-label mb-4'}))
