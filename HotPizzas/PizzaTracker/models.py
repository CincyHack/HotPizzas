from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
	user = models.OneToOneField(User)
	phone_number = models.CharField(max_length=15)
	latitude = models.DecimalField(
		max_digits=20,
		decimal_places=17
	)
	longitude = models.DecimalField(
		max_digits=20,
		decimal_places=17
	)
	last_location_time = models.DateTimeField()
	

class Driver(models.Model):
	user = models.OneToOneField(User)
	latitude = models.DecimalField(
		max_digits=20,
		decimal_places=17
	)
	longitude = models.DecimalField(
		max_digits=20,
		decimal_places=17
	)
	last_location_time = models.DateTimeField()
	

class Pizza(models.Model):
	CHEESE = "C"
	PEPPERONI = "P"
	SAUSAGE = "S"
	TOPPING_CHOICES = (
		(CHEESE, "Cheese"),
		(PEPPERONI, "Pepperoni"),
		(SAUSAGE, "Sausage"),
	)
	cook_time = models.DateTimeField()
	price = models.DecimalField(max_digits=4, decimal_places=2)
	topping = models.CharField(max_length=1, choices=TOPPING_CHOICES, default=CHEESE)
	customer = models.ForeignKey(Customer, null=True, blank=True)
	driver = models.ForeignKey(Driver)
	
