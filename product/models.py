from django.db import models

class Product(models.Model):

	barcode = models.IntegerField(max_length=20)
	price = models.IntegerField(max_length=20)
	name = models.CharField(max_length=20)
	

