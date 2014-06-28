from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Customer(AbstractBaseUser):
	
	class Meta:
		app_label = "core"

	phone_number = models.CharField(max_length=15, primary_key=True)
	name = models.CharField(max_length=100)

	def __str__(self):
		return str(self.phone_number) + ": " + str(self.name)


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

