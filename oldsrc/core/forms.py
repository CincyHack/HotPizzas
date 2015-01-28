from datetime import datetime
from django import forms
from .models import Pizza, HotPizzasUser

		
class CustomerForm(forms.ModelForm):
	phone_number = forms.RegexField(
		regex=r'^\+?1?\d{9,15}$', 
		error_message=("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	)
	class Meta:
		model = Customer
		fields = ('phone_number')

	
class PizzaForm(forms.ModelForm):
	cook_time = forms.DateTimeField(initial=datetime.now())
	price = forms.DecimalField(max_digits=4, decimal_places=2)
	#FIXME: implement choices from db select
	#topping = forms.ChoiceField(Pizza.TOPPING_CHOICES)
	class Meta:
		model = Pizza
		fields = (
			'cook_time',
			'price',
			#'topping'
		)
		
class DriverForm(forms.ModelForm):

	class Meta:
		model = Driver
		fields = ()

