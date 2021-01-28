from django.db import models
from django.urls import reverse

# Create your models here.
# Want out backend to have a memory of a product created
# Layers of database with django/python 1. Django/Python Layer This doesn't require migration. 
# 2. Database Layer: This requires migration
class Product(models.Model):
	# This creates a database using the DDL from 3DB3 rememeber. 
	# And assigns the column witht he right datatypes
	title 		= models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price 		= models.DecimalField(decimal_places=2, max_digits=10000)
	summary 	= models.TextField(blank=True, null=True)
	featured 	= models.BooleanField(default=True )

	# an instance method for getting the url for any products 
	# related to oiur model
	def get_absolute_url_without_reverse(self):
		# return f'/products/{self.id}'
		return '/products/{}'.format(self.id)

	# Using reverse method to make URLs dynamic
	def get_absolute_url(self):
		# return f'/products/{self.id}'
		# return '/products/{}'.format(self.id))
		return reverse("products:product-lookup", kwargs={'my_id': self.id})