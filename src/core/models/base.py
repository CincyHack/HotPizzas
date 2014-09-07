from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class HotPizzasUser(AbstractUser):

	class Meta:
		app_label = "core"

	is_customer = models.BooleanField(default=True)
	is_driver = models.BooleanField(default=False)
	phone_number = models.CharField(max_length=15)
	name = models.CharField(max_length=100)
	longitude = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
	latitude = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
	last_location = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return str(self.name)


