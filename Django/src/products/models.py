from django.db import models

# Create your models here.
# Want out backend to have a memory of a product created
class Product(models.Model):
	# This creates a database using the DDL from 3DB3 rememeber. 
	# And assigns the column witht he right datatypes
	title 		= models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price 		= models.DecimalField(decimal_places=2, max_digits=10000)
	summary 	= models.TextField(blank=True, null=True)
	featured 	= models.BooleanField(default=True )