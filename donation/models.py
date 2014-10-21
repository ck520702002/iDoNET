from django.db import models
from django.utils import timezone
import product

class donation_detail(models.Model):

	amount = models.IntegerField(max_length=10,blank=False)
	detail = models.ForeignKey('product.product')
	time = models.DateTimeField(auto_now=True)
	charity = models.ForeignKey("donation.Charities")
	

class Charities(models.Model):
	
	name = models.CharField(max_length=20,blank=False) 
	intro = models.CharField(max_length=200,blank=True) 