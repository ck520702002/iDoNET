from django.db import models
from django.utils import timezone
from product.models import Product
from django.contrib.auth.models import User
from django.db.models import Sum

class Charity(models.Model):
	name = models.CharField(max_length=20,blank=False) 
	intro = models.CharField(max_length=200,blank=True) 
	category = models.CharField(max_length=20,blank=True)
	link = models.URLField(blank=True)
	def __unicode__(self):  
          return self.name 

class Invoice(models.Model):
	owner = models.ForeignKey(User)
	number = models.CharField(max_length=20,blank=False) 
	product = models.ManyToManyField(Product)
	time = models.DateTimeField(auto_now=True)
	to_whom = models.ForeignKey(Charity)
	total_price = models.IntegerField(max_length=10,blank=True,null=True)
	hit = models.BooleanField()

	def get_price(self):
		price = Product.objects.filter(invoice__id=self.pk).aggregate(Sum('price'))
		return price

	def __unicode__(self):  
	    return self.number 

class Donation_detail(models.Model):
	owner = models.ForeignKey(User)
	threshold = models.IntegerField(max_length=20,null=True)
	roundup = models.IntegerField(max_length=20,null=True)
	amount = models.IntegerField(max_length=10,blank=True,null=True)
	invoice = models.ForeignKey(Invoice)
	time = models.DateTimeField(auto_now=True)
	to_whom = models.ForeignKey(Charity)
	Donation_detailamount = models.IntegerField(max_length=10,blank=True,null=True)


