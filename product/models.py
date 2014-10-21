from django.db import models

class Product(models.Model):

	barcode = models.IntegerField()
	price = models.IntegerField()
	name = models.CharField(max_length=20,blank=False)
	

