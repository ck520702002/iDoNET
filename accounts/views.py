# -*- coding: utf-8 -*-
from django import forms
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from forms import login_form,sign_up_form
from django.contrib.auth.models import User
from iDoNET.utils import get_alert_box
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
			        return redirect("/")
			    else:
			    	html = get_alert_box("哈囉你還沒被啟用",request)
		        	return HttpResponse(html)
			else:
			    # the authentication system was unable to verify the username and password
			    html = get_alert_box("哈囉你還沒申請吧",request)
		        return HttpResponse(html)

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

			user = authenticate(username=username, password=password)
			django_login(request, user)
			return redirect("/")
		
class logout(View):
	def get(self, request, *args, **kwargs):
		django_logout(request)
		return redirect("/")

class setting(TemplateView):
	template_name = "info.html"
	
