from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class AutomatoUser(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Invalid phone number."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        blank=True,
        max_length=17
    )
