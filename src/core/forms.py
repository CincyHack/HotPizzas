from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from .models import Pizza, Customer, Driver


class LocationForm(forms.Form):
	latitude = forms.DecimalField(widget=forms.HiddenInput(), max_digits=20, decimal_places=17)
	longitude = forms.DecimalField(widget=forms.HiddenInput(), max_digits=20, decimal_places=17)


class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Please enter a username.")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")
	first_name = forms.CharField()
	last_name = forms.CharField()

	class Meta:
		model = User
		fields = ('username', 'password', 'first_name', 'last_name')
		
class CustomerForm(forms.ModelForm):
	phone_number = forms.RegexField(
		regex=r'^\+?1?\d{9,15}$', 
		error_message=("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	)
	latitude = forms.DecimalField(widget=forms.HiddenInput(), max_digits=20, decimal_places=17)
	longitude = forms.DecimalField(widget=forms.HiddenInput(), max_digits=20, decimal_places=17)
	
	class Meta:
		model = Customer
		fields = ('phone_number', 'latitude', 'longitude')
		
class PizzaForm(forms.ModelForm):
	cook_time = forms.DateTimeField(initial=datetime.now())
	price = forms.DecimalField(max_digits=4, decimal_places=2)
	topping = forms.ChoiceField(Pizza.TOPPING_CHOICES)
	class Meta:
		model = Pizza
		fields = ('cook_time', 'price', 'topping')
		
class DriverForm(forms.ModelForm):
	latitude = forms.DecimalField(widget=forms.HiddenInput(), max_digits=20, decimal_places=17)
	longitude = forms.DecimalField(widget=forms.HiddenInput(), max_digits=20, decimal_places=17)
	
	class Meta:
		model = Driver
		fields = ('latitude', 'longitude')

