from django.forms import ModelForm
from django.contrib.auth.models import User
from PizzaTracker.models import *
from datetime import datetime

class UserForm(ModelForm):
	username = forms.CharField(help_text="Please enter a username.")
	email = forms.EmailField(help_text="Please enter your email.")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class CustomerForm(ModelForm):
	phone_number = forms.RegexField(
		regex=r'^\+?1?\d{9,15}$', 
		error_message=("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	)
	latitude = forms.DecimalField(widget=forms.HiddenInput(), max_digits=20, decimal_places=17)
	longitude = forms.DecimalField(widget=forms.HiddenInput(), max_digits=20, decimal_places=17)
	
	class Meta:
		model = Customer
		fields = ('phone_number', 'latitude', 'logitude')
		
class PizzaForm(ModelForm):
	cook_time = forms.DateTimeField(initial=datetime.now())
	price = forms.DecimalField(max_digits=4, decimal_places=2)
	topping = forms.ChoiceField(Pizza.TOPPING_CHOICES)
	class Meta:
		model = Pizza
		fields = ('cook_time', 'price', 'topping')
		
class DriverForm(ModelForm):
	latitude = forms.DecimalField(widget=forms.HiddenInput(), max_digits=20, decimal_places=17)
	longitude = forms.DecimalField(widget=forms.HiddenInput(), max_digits=20, decimal_places=17)
	
	class Meta:
		model = Driver
		fields = ('latitude', 'longitude')

