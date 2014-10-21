from django.db import models

class Product(models.Model):

	barcode = models.integerfield()
	price = models.integerfield()
	name = models.CharField()
	

