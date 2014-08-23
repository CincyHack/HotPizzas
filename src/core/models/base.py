from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Location(models.Model):
	
	class Meta:
		app_label = "core"
		
	longitude = models.DecimalField(max_digits=10, decimal_places=5)
	latitude = models.DecimalField(max_digits=10, decimal_places=5)
	
	def __str__(self):
		return "(" + str(self.longitude) + ", " + str(self.latitude) + ")"


class Customer(AbstractBaseUser):
	
	class Meta:
		app_label = "core"

	phone_number = models.CharField(max_length=15, primary_key=True)

	def __str__(self):
		return str(self.phone_number)


class CustomerInformation(models.Model):
	
	class Meta:
		app_label = "core"
		
	name = models.CharField(max_length=100)
	customer = models.ForeignKey(Customer, related_name='customer_informations')
	location = models.ForeignKey(Location, related_name='customer')

	def __str__(self):
		return str(self.name)


class Driver(AbstractBaseUser):
	class Meta:
		app_label = "core"

	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)
	phone_number = models.CharField(max_length=15)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	def __str__(self):
		return str(self.email)

