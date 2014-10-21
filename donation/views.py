from django.shortcuts import render
from django.views.generic import View
from invoice.models import Invoice
from product.models import Product

class DonationView(View):
	template_name = 'query1.html'
	def get(self, request, *args, **kwargs):
		x = Invoice.objects.all()
		y = Product.objects.all()
		return render(request,self.template_name,{'invoice':x,'product':y})

