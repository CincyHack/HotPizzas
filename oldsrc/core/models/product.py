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
		permissions = (
			('view_product', 'view product'),
		)

	cook_time = models.DateTimeField()
	expiration_time = models.DateTimeField()
	base_price = models.DecimalField(max_digits=4, decimal_places=2)
	product_type = models.ForeignKey(ProductType)
	configurations = models.ManyToManyField(ProductConfiguration)
	#30 sep 2014 - FIXME: remove customer for anon-first
	#customer = models.ForeignKey(HotPizzasUser, null=True, blank=True, related_name='products-orders')
	purchased = models.BooleanField(default=False)
	customer_sessionid = models.CharField(max_length=32, null=True, blank=True)
	customer_phone_number = models.CharField(max_length=15, null=True, blank=True)
	customer_longitude = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
	customer_latitude = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
	customer_name = models.CharField(max_length=100, null=True, blank=True)

	driver = models.ForeignKey(HotPizzasUser, related_name='products-deliveries')
	delivered = models.BooleanField(default=False)
	request_time = models.DateTimeField(null=True, blank=True)
	deliverable_range = models.IntegerField(null=True, blank=True, default=10)
	delivered_longitude = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
	delivered_latitude = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
	

	def __str__(self):
		return str(self.product_type) + str(self.id)

	def clean(self):
		is_error = False
		err_str = []

		if not self.driver.is_driver:
			is_error = True
			err_str.append("Product must have driver and driver user must be a driver")
		
		#FIXME: put this back in with customer and remove following
		#if self.customer and not self.customer.is_customer:
		#	is_error = True
		#	err_str.append("Product customer user must be a customer")
		purchase_fields = [
			self.purchased,
			self.customer_phone_number,
			self.customer_latitude,
			self.customer_longitude,
			self.customer_name,
		]

		if any(purchase_fields) and not all(purchase_fields):
			if self.customer_phone_number in [None, '']:
				is_error = True
				err_str.append("Product must have a customer phone number to be purchased")
			
			if self.customer_latitude == None:
				is_error = True
				err_str.append("Product must have a customer latitude to be purchased")

			if self.customer_longitude == None:
				is_error = True
				err_str.append("Product must have a customer longitude to be purchased")

			if self.customer_name in [None, '']:
				is_error = True
				err_str.append("Product must have a customer name to be purchased")

			if not self.purchased:
				is_error = True
				err_str.append("Product must have purchase set to True to be purchased")


		if is_error:
			raise ValidationError((", ".join(err_str) + "."))


