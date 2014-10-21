from django.db import models

class Product(models.Model):

	barcode = models.IntegerField()
	price = models.IntegerField()
	name = models.CharField()
	

