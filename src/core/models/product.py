from django.db import models
from django.core.exceptions import ValidationError
from .base import HotPizzasUser


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
	customer = models.ForeignKey(HotPizzasUser, null=True, blank=True, related_name='products-orders')
	driver = models.ForeignKey(HotPizzasUser, related_name='products-deliveries')
	delivered = models.BooleanField(default=False)
	request_time = models.DateTimeField(null=True, blank=True)
	delivered_longitude = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
	delivered_latitude = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
	

	def __str__(self):
		return str(self.product_type) + str(self.id)

	def clean(self):
		is_error = False
		err_str = []

		if not self.driver.is_driver:
			is_error = True
			err_str.append("Product driver user must be a driver")

		if self.customer and not self.customer.is_customer:
			is_error = True
			err_str.append("Product customer user must be a customer")

		if is_error:
			raise ValidationError((", ".join(err_str) + "."))

