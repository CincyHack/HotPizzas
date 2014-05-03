from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from PizzaTracker.models import *

def home(request):
	return HttpResponse("Hello World")

@login_required
def available_pizzas(request):
	pizzas = [
		{
			"cook_time": str(pizza.cook_time),
			"price": pizza.price,
			"topping": pizza.topping,
			"customer_username": pizza.customer.username,
			"customer_phone": pizza.customer.phone_number,
		} for pizza in Pizza.objects.select_related().filter(driver=request.user.id)
	]
	return HttpResponse(str(pizzas))

@login_required
def buy_pizza(request):
	pass
