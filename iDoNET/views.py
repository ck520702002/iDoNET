# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.
class home(View):
	template = "home.html"
	def get(self, request, *args, **kwargs):
		return HttpResponse('哈囉我是轟配擠')