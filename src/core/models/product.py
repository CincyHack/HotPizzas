from django.db import models
from .base import Driver, Customer


class ProductType(models.Model):

	class Meta:
		app_label = "core"

	name = models.CharField(max_length=20, primary_key=True)

	def __str__(self):
		return str(self.name)

	
class ProductConfiguration(models.Model):

	class Meta:
		app_label = "core"

	description = models.CharField(max_length=50)
	product_type = models.ForeignKey(ProductType)

	def __str__(self):
		return str(self.product_type) + ": " + str(self.description)


class Product(models.Model):
	
	class Meta:
		app_label = "core"

	cook_time = models.DateTimeField()
	expiration_time = models.DateTimeField()
	base_price = models.DecimalField(max_digits=4, decimal_places=2)
	product_type = models.ForeignKey(ProductType)
	configurations = models.ManyToManyField(ProductConfiguration)
	customer = models.ForeignKey(Customer, null=True, blank=True, related_name='products')
	driver = models.ForeignKey(Driver, related_name='products')
	delivered = models.BooleanField(default=False)
	request_time = models.DateTimeField(null=True, blank=True)
	

	def __str__(self):
		return str(self.product_type) + str(self.id)

