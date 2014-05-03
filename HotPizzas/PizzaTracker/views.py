from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from PizzaTracker.models import *

def home(request):
	return HttpResponse("Hello World")

@login_required
def available_pizzas(request):
	pizzas = list()
	for pizza in Pizza.objects.select_related().filter(delivered=False).filter(driver=request.user.id):
		formatted_pizza = pizza_to_dict(pizza, customer=False)
		pizzas.append(formatted_pizza)

	return HttpResponse(str(pizzas))

@login_required
def delivered_pizzas(request):
	pizzas = list()
	for pizza in Pizza.objects.select_related().filter(delivered=True).filter(driver=request.user.id):
		formatted_pizza = pizza_to_dict(pizza)
		pizzas.append(formatted_pizza)
		
	return HttpResponse(str(pizzas))

@login_required
def to_deliver_pizzas(request):
	pizzas = list()
	for pizza in Pizza.object.select_related().filter(delivered=False).filter(driver=request.user.id):
		formatted_pizza = pizza_to_dict(pizza, customer=False)
		pizzas.append(formatted_pizza)
		
	return HttpResponse(str(pizzas))

def pizza_to_dict(pizza, customer=True):
	formatted_pizza = dict()
	formatted_pizza["cook_time"] = str(pizza.cook_time)
	formatted_pizza["price"] = str(pizza.price)
	formatted_pizza["topping"] = pizza.topping
	if customer and pizza.customer:
		formatted_pizza["customer_username"] = pizza.customer.username
		formatted_pizza["customer_phone"] = pizza.customer.phone
	elif customer:
		formatted_pizza["customer_username"] = ""
		formatted_pizza["customer_phone"] = ""
	
	return formatted_pizza

@login_required
def buy_pizza(request):
	pass
