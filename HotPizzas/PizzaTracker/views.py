from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from PizzaTracker.models import *

@login_required
def driver_dashboard(request):
	pizzas_available = pizza_to_dict(request.user.id, delivered=False, customer=False)
	pizzas_delivered = pizza_to_dict(request.user.id, delivered=True)
	pizzas_to_deliver = pizza_to_dict(request.user.id, customer=True, delivered=False)
	ctx = {'pizzas_available': pizzas_available, 'pizzas_delivered': pizzas_delivered, 'pizzas_to_deliver': pizzas_to_deliver }
	
	return render(request, 'driver-pizzas.html', ctx)

def home(request):
	return HttpResponse('Hello World')
	

@login_required
def available_pizzas(request):
	pizzas = pizza_to_dict(request.user.id, delivered=False, customer=False)
	return HttpResponse(str(pizzas))

@login_required
def delivered_pizzas(request):
	pizzas = pizza_to_dict(request.user.id, delivered=True)
	return HttpResponse(str(pizzas))

@login_required
def to_deliver_pizzas(request):
	pizzas = pizza_to_dict(request.user.id, customer=False, delivered=False)
	return HttpResponse(str(pizzas))

def pizza_to_dict(user_id, customer=True, delivered=False):
	pizzas = list()
	
	for pizza in Pizza.objects.select_related().filter(delivered=delivered).filter(driver__user_id=user_id):
		formatted_pizza = dict()
		formatted_pizza["cook_time"] = str(pizza.cook_time)
		formatted_pizza["price"] = str(pizza.price)
		formatted_pizza["topping"] = pizza.topping
		if pizza.customer != None:
			formatted_pizza["customer_username"] = pizza.customer.user.username
			formatted_pizza["customer_phone"] = pizza.customer.phone
			formatted_pizza["customer_latitude"] = pizza.customer.latitude
			formatted_pizza["customer_longitude"] = pizza.customer.longitude
			if pizza.customer.user.lastname != None and pizza.customer.user.firstname != None:
				formatted_pizza["customer_fistname"] = pizza.customer.user.firstname + pizza.customer.user.lastname
			else:
				formatted_pizza["customer_fullname"] = ""

		else:
			formatted_pizza["customer_username"] = ""
			formatted_pizza["customer_phone"] = ""
			formatted_pizza["customer_fullname"] = ""
	
		if pizza.customer == None and customer == False:
			pizzas.append(formatted_pizza)
		elif pizza.customer != None and customer == True:
			pizzas.append(formatted_pizza)
			
	return pizzas

@login_required
def buy_pizza(request):
	pass
