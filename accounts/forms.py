# -*- coding: utf-8 -*-
from django import forms

class login_form(forms.Form):
    username = forms.IntegerField(label='卡號')
    password = forms.CharField(label='密碼',widget=forms.PasswordInput)

class sign_up_form(forms.Form):
    username = forms.IntegerField(label='卡號')
    password = forms.CharField(label='密碼',widget=forms.PasswordInput)
    password_again = forms.CharField(label='確認密碼',widget=forms.PasswordInput)