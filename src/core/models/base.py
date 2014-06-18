from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User


class HotPizzasUserManager(BaseUserManager):
	class Meta:
		app_label = "core"


class HotPizzasUser(AbstractBaseUser):
	class Meta:
		app_label = "core"

	objects = HotPizzasUserManager()
	phone_number = models.ChaarField(max_length=15)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_customer = models.BooleanField(default=True)
	is_driver = models.BooleanField(default=False)

class Customer(models.Model):
	
	class Meta:
		app_label = "core"

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
	
	def __str__(self):
		return str(self.user)
	

class Driver(models.Model):

	class Meta:
		app_label = "core"

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
	
	def __str__(self):
		return str(self.user)
