# -*- coding: utf-8 -*-
from django import forms

class login_form(forms.Form):
    username = forms.CharField(label='卡號')
    password = forms.CharField(label='密碼',widget=forms.PasswordInput)

class sign_up_form(forms.Form):
<<<<<<< HEAD
    username = forms.IntegerField(label='卡號')
    password = forms.CharField(label='密碼',widget=forms.PasswordInput)
    password_again = forms.CharField(label='確認密碼',widget=forms.PasswordInput)
=======
    username = forms.CharField(label='卡號')
    password = forms.CharField(label='密碼',widget=forms.PasswordInput)
>>>>>>> 04780fbcc9d201b639de3dafba81847b9f7f88fc
