# -*- coding: utf-8 -*-
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from forms import login_form,sign_up_form
from django.contrib.auth.models import User

# Create your views here.
class login(View):
	def get(self, request, *args, **kwargs):
		form = login_form()
		return render(request, 'accounts/login.html', {'form': form})

	def post(self, request, *args, **kwargs):
		form = login_form(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
			    # the password verified for the user
			    if user.is_active:
			    	django_login(request, user)
			        return HttpResponse('哈囉你有權限')
			    else:
			        return HttpResponse('哈囉你還沒被啟用')
			else:
			    # the authentication system was unable to verify the username and password
			    return HttpResponse('哈囉你還沒申請吧')

class signup(View):
	def get(self, request, *args, **kwargs):
		form = sign_up_form()
		return render(request, 'accounts/sign_up.html', {'form': form})

	def post(self, request, *args, **kwargs):
		form = sign_up_form(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = User.objects.create_user(username, '', password)
			user.save()
			message = '申請成功囉，你的卡號是',username
			return HttpResponse(message)
		
class logout(View):
	def get(self, request, *args, **kwargs):
		django_logout(request)
		return HttpResponse('你登出囉呵呵')
