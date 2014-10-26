from django.shortcuts import render,redirect
from django.views.generic import View
from donation.models import Invoice
from donation.models import Donation_detail
from product.models import Product
from models import Charity
from accounts.models import UserProfile

class QueryView(View):
	template_name = 'query1.html'
	def get(self, request, *args, **kwargs):
		x = Invoice.objects.all()
		for q in x:
			q.total_price = q.get_price()['price__sum']
		y = Product.objects.all()
		details = Donation_detail.objects.all()
		for detail in details:
			invoice = x.get(id=detail.invoice.id)
			detail.amount = invoice.get_price()['price__sum']
			detail.Donation_detailamount = detail.roundup-(detail.amount % detail.roundup)
		return render(request,self.template_name,{'invoices':x,'products':y,'details':details})

def get(self, request, *args, **kwargs):
		details = Donation_detail.objects.all()
		invoices = Invoice.objects.all()
		for detail in details:
			invoice = invoices.get(id=detail.invoice)
			detail.amount = invoice.get_price()['price__sum']
			detail.Donation_detailamount = detail.roundup-(detail.amount % detail.roundup)
		return render(request,self.template_name, {'details':details})

class DonateInvoiceView(View):
	template_name = 'invoice1.html'
	def get(self, request, *args, **kwargs):
		charities = list(Charity.objects.all())
		attr =[]
		for charity in charities:
			attr.append(charity.category)
		categories = list(set(attr))
		return render(request,self.template_name,{'categories':categories})

	def post(self, request, *args, **kwargs):
		if 'chosen_category' in request.POST:
			search_charities = list(Charity.objects.filter(category = request.POST['chosen_category']))
			charities = list(Charity.objects.all())
			attr =[]
			for charity in charities:
				attr.append(charity.category)
			categories = list(set(attr))
			return render(request,self.template_name,{'search_charities':search_charities,'categories':categories})

		elif 'chosen_charity' in request.POST:
			user_profile = UserProfile.objects.get(user=request.user.id) 
			user_profile.card_number = request.POST['card_number']
			user_profile.favored_charity = Charity.objects.get(pk=request.POST['chosen_charity'])
			return redirect('/')
			


class DonateCoinView(View):
	template_name = 'coin1.html'
	def get(self, request, *args, **kwargs):
		details = Donation_detail.objects.filter()

		for detail in details:
			detail.amount = detail.invoice.get_price()['price__sum']
			detail.Donation_detailamount = detail.roundup-(detail.amount % detail.roundup)

		return render(request,self.template_name, {'details':details})
