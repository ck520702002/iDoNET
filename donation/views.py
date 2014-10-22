from django.shortcuts import render
from django.views.generic import View
from donation.models import Invoice
from product.models import Product

class QueryView(View):
	template_name = 'query1.html'
	def get(self, request, *args, **kwargs):
		x = Invoice.objects.all()
		y = Product.objects.all()
		return render(request,self.template_name,{'invoices':x,'products':y})

class DonateInvoiceView(View):
	template_name = 'invoice1.html'
	def get(self, request, *args, **kwargs):
		invoices = Invoice.objects.filter()
		return render(request,self.template_name,{'invoices':invoices})

class DonateCoinView(View):
	template_name = 'coin1.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name)
