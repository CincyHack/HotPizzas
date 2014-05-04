from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from PizzaTracker.models import *

@login_required
def driver_dashboard(request):
	pizzas_available = list()
	for pizza in Pizza.objects.select_related().filter(delivered=False).filter(driver__user_id=request.user.id):
		formatted_pizza = pizza_to_dict(pizza, customer=False)
		pizzas_available.append(formatted_pizza)
	
	pizzas_delivered = list()
	for pizza in Pizza.objects.select_related().filter(delivered=True).filter(driver__user_id=request.user.id):
		formatted_pizza = pizza_to_dict(pizza)
		pizzas_delivered.append(formatted_pizza)
		
	pizzas_to_deliver = list()
	for pizza in Pizza.objects.select_related().filter(delivered=False).filter(driver__user_id=request.user.id):
		formatted_pizza = pizza_to_dict(pizza, customer=False)
		pizzas_to_deliver.append(formatted_pizza)
	
	ctx = {'pizzas_available': pizzas_available, 'pizzas_delivered': pizzas_delivered, 'pizzas_to_deliver': pizzas_to_deliver }
	
	return render(request, 'driver-pizzas.html', ctx)

def home(request):
	return HttpResponse('Hello World')
	

@login_required
def available_pizzas(request):
	pizzas = list()
	for pizza in Pizza.objects.select_related().filter(delivered=False).filter(driver__user_id=request.user.id):
		formatted_pizza = pizza_to_dict(pizza, customer=False)
		pizzas.append(formatted_pizza)

	return HttpResponse(str(pizzas))

@login_required
def delivered_pizzas(request):
	pizzas = list()
	for pizza in Pizza.objects.select_related().filter(delivered=True).filter(driver__user_id=request.user.id):
		formatted_pizza = pizza_to_dict(pizza)
		pizzas.append(formatted_pizza)
		
	return HttpResponse(str(pizzas))

@login_required
def to_deliver_pizzas(request):
	pizzas = list()
	for pizza in Pizza.objects.select_related().filter(delivered=False).filter(driver__user_id=request.user.id):
		formatted_pizza = pizza_to_dict(pizza, customer=False)
		pizzas.append(formatted_pizza)
		
	return HttpResponse(str(pizzas))

def pizza_to_dict(pizza, customer=True):
	formatted_pizza = dict()
	formatted_pizza["cook_time"] = str(pizza.cook_time)
	formatted_pizza["price"] = str(pizza.price)
	formatted_pizza["topping"] = pizza.topping
	if customer and pizza.customer != None:
		formatted_pizza["customer_username"] = pizza.customer.user.username
		formatted_pizza["customer_phone"] = pizza.customer.phone
		formatted_pizza["customer_latitude"] = pizza.customer.latitude
		formatted_pizza["customer_longitude"] = pizza.customer.longitude
		if pizza.customer.user.lastname != None and pizza.customer.user.firstname != None:
			formatted_pizza["customer_fistname"] = pizza.customer.user.firstname + pizza.customer.user.lastname
		else:
			formatted_pizza["customer_fullname"] = ""

	elif customer:
		formatted_pizza["customer_username"] = ""
		formatted_pizza["customer_phone"] = ""
		formatted_pizza["customer_fullname"] = ""
	
	return formatted_pizza

@login_required
def buy_pizza(request):
	pass
