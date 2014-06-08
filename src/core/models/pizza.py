from django.db import models
from django.contrib.auth.models import User
from .models import Driver, Customer

class PizzaManager(models.Manager):
	use_for_related_fields = True
	
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
	delivered = models.BooleanField(default=False)
	request_time = models.DateTimeField(null=True, blank=True)
	
	objects = PizzaManager()
	
	def __str__(self):
		return str(self.driver) + " " + str(self.topping) + str(self.id)
