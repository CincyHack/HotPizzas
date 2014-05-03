from django.db import models
from django.contrib.auth import User


# Create your models here.
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
	price = models.DecimalField(max_digits=4, decimal_digits=2)
	topping = models.CharField(max_length=1, choices=TOPPING_CHOICES, default=CHEESE)
	buyer = models.ForeignKey(User, related_name="buyer")
	driver = models.ForeignKey(Driver)
	
class Driver(models.Mode):
	user = models.OneToOneField(User)
	latitude = models.DecimalField(
		max_digits=10,
		decimal_places=5
	)
	longitude = models.DecimalField(
		max_digits=10,
		decimal_places=5
	)
	last_location_time = models.DateTimeField()
	
