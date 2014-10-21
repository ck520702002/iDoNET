from django.db import models
from product import Product
import product

class Invoice(models.Model)	
	
	number = models.CharField(max_length=20,blank=False) 
	product = models.ManyToMany('product.Product') 
	def get_price():
		Product.objects.filter(invoice__id=self.pk)
