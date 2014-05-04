from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from PizzaTracker.models import *
from PizzaTracker.forms import *

@login_required
def customer_dashboard(request):
	return HttpResponse("I'm not done")
	
def anonymous_pizza_browser(request):
	if request.method == POST:
		form = LocationForm(request.POST)
		if form.is_valid():
			close_pizzas = Pizza.objects.select_related().filter(customer__isnull=true)
			#TODO: return these close pizzas to display.
			
	else:
		form = LocationForm()
		
	return render(request, 'anon-browser.html', {'form': form})

@login_required
def driver_dashboard(request):
	pizzas_available = pizza_to_dict(request.user.id, delivered=False, customer=False)
	pizzas_delivered = pizza_to_dict(request.user.id, delivered=True)
	pizzas_to_deliver = pizza_to_dict(request.user.id, customer=True, delivered=False)
	ctx = {'pizzas_available': pizzas_available, 'pizzas_delivered': pizzas_delivered, 'pizzas_to_deliver': pizzas_to_deliver }
	
	return render(request, 'driver-pizzas.html', ctx)

def home(request):
	if request.user.is_authenticated():
		if len(list(Driver.objects.filter(user=request.user.id))) != 0:
			return HttpResponseRedirect('/driver/')
		else:
			return HttpResponseRedirect('/customer/')
	else:
		return HttpResponse("Hype page goes here")
	

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
	pizzas = pizza_to_dict(request.user.id, customer=True, delivered=False)
	return HttpResponse(str(pizzas))

def pizza_to_dict(user_id, customer=True, delivered=False):
	pizzas = list()
	
	for pizza in Pizza.objects.select_related().filter(delivered=delivered).filter(driver__user_id=user_id):
		formatted_pizza = dict()
		formatted_pizza["cook_time"] = str(pizza.cook_time)
		formatted_pizza["price"] = str(pizza.price)
		formatted_pizza["topping"] = pizza.get_topping_display()
		if pizza.request_time:
			formatted_pizza["request_time"] = str(pizza.request_time)
		else:
			formatted_pizza["request_time"] = ""

		if pizza.customer:
			formatted_pizza["customer_username"] = pizza.customer.user.get_username()
			formatted_pizza["customer_phone"] = pizza.customer.phone_number
			formatted_pizza["customer_latitude"] = pizza.customer.latitude
			formatted_pizza["customer_longitude"] = pizza.customer.longitude
			if pizza.customer.user.last_name and pizza.customer.user.first_name:
				formatted_pizza["customer_fullname"] = pizza.customer.user.first_name \
				+ " " \
				+ pizza.customer.user.last_name
			else:
				formatted_pizza["customer_fullname"] = ""

		else:
			formatted_pizza["customer_username"] = ""
			formatted_pizza["customer_phone"] = ""
			formatted_pizza["customer_fullname"] = ""
	
		if pizza.customer and not customer:
			pizzas.append(formatted_pizza)
		elif pizza.customer and customer:
			pizzas.append(formatted_pizza)
			
	return pizzas

@login_required
def buy_pizza(request):
	pass
