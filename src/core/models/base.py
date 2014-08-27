from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Location(models.Model):
	
	class Meta:
		app_label = "core"
		
	longitude = models.DecimalField(max_digits=10, decimal_places=5)
	latitude = models.DecimalField(max_digits=10, decimal_places=5)
	
	def __str__(self):
		return "(" + str(self.latitude) + ", " + str(self.longitude) + ")"


class HotPizzasUser(AbstractUser):

	class Meta:
		app_label = "core"

	is_customer = models.BooleanField(default=True)
	is_driver = models.BooleanField(default=False)
	phone_number = models.CharField(max_length=15)
	name = models.CharField(max_length=100)
	location = models.ForeignKey(Location, related_name='user')

	def __str__(self):
		return str(self.name)


