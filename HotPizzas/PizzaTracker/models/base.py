from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser


class Customer(AbstractBaseUser):
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
	

class Driver(AbstractBaseUser):
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
