from django.forms import ModelForm
from django.contrib.auth.models import User
from PizzaTracker.models import *

class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Please enter a username.")
	email = forms.EmailField(help_text="Please enter your email.")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class CustomerForm(forms.ModelForm):
	phone_number = forms.RegexField(
		regex=r'^\+?1?\d{9,15}$', 
		error_message=("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	)
	latitude = forms.DecimalForm()
	longitude = forms.DecimalForm()
	
	class Meta:
		model = Customer
		fields = ('phone_number', 'latitude', 'logitude')
		
class PizzaForm(forms.ModelForm):
	class Meta:
		model = Pizza
		fields = ('cook_time', 'price', 'topping')
		
class DriverForm(forms.ModelForm):
	class Meta:
		model = Driver
		fields = ('latitude', 'longitude')
