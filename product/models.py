from django.db import models

class Product(models.Model):

	barcode = models.IntegerField(max_length=20,blank=False)
	price = models.IntegerField(max_length=20,blank=False)
	name = models.CharField(max_length=20,blank=False)
	

