from django.shortcuts import render

class DonationView(View):
	template_name = 'query1.html'
	def get(self, request, *args, **kwargs):
	x = Invoice.objects.all()
	y = Product.objects.all()
	return render(request,self.template_name,{'invoice':x,'product':y})

