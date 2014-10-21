from django.db import models
from product import Product
import product

class invoice(models.Model)	
	
	number = models.CharField(max_length=20,blank=False)
	def get_price():
		Product.objects.filter(pk=self.pk)
