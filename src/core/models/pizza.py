from django.db import models
from django.contrib.auth.models import User
from .base import Driver, Customer

class Topping(models.Model):

	class Meta:
		app_label = "core"

	name = models.CharField(max_length=20)

class PizzaManager(models.Manager):
	use_for_related_fields = True
	
class Pizza(models.Model):
	
	class Meta:
		app_label = "core"

	cook_time = models.DateTimeField()
	price = models.DecimalField(max_digits=4, decimal_places=2)
	toppings = models.ManyToManyField(Topping)
	customer = models.ForeignKey(Customer, null=True, blank=True)
	driver = models.ForeignKey(Driver)
	delivered = models.BooleanField(default=False)
	request_time = models.DateTimeField(null=True, blank=True)
	
	objects = PizzaManager()
	
	def __str__(self):
		string = "{}: A pizza, cooked at {}, being delivered by {}"
		string = string.format(
			str(self.id),
			str(self.cook_time),
			str(self.driver)
		)
		return string 
