from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class HotPizzasUserManager(BaseUserManager):
	class Meta:
		app_label = "core"


class HotPizzasUser(AbstractBaseUser):
	class Meta:
		app_label = "core"

	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)
	phone_number = models.ChaarField(max_length=15)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_customer = models.BooleanField(default=True)
	is_driver = models.BooleanField(default=False)

	objects = HotPizzasUserManager()
	
	USERNAME_FIELD = 'email'
	
	def __str__(self):
		return str(self.username)

