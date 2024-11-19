from django import forms
from django.forms import models


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(max_length=8, label='Введите пароль:', widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=8, label='Подтвердите пароль:', widget=forms.PasswordInput)
    age = forms.CharField(max_length=3, label='Введите свой возраст:')
