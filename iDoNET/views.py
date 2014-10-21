# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.
class home(View):
	template_name = "home.html"
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)