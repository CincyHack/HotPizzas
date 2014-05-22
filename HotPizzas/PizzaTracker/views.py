from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from PizzaTracker.models import *
from PizzaTracker.forms import *
import json
import string
from datetime import datetime
from django.contrib.auth import authenticate
from django.db.models import Q


def update_pizza(request):
	if request.user.is_authenticated():
		if request.is_ajax() and request.method == 'POST':
			if request.POST.get("pizza_id")\
			and request.POST.get("longitude")\
			and request.POST.get("latitude"):
				pizza = Pizza.objects.get(id=request.POST["pizza_id"])
				pizza.customer = Customer.get(user__id = request.user.id)
				pizza.save()
				return HttpResponse(json.dumps({"was_bought": True}), content_type="application/json")
				
	else:
		if request.is_ajax() and request.method == 'POST':
			if request.POST.get("first_name")\
			and request.POST.get("last_name")\
			and request.POST.get("phone_number")\
			and request.POST.get("pizza_id")\
			and request.POST.get("longitude")\
			and request.POST.get("latitude")\
			and request.POST.get("username")\
			and request.POST.get("password"):
				user_form = UserForm(
					{
						'first_name': request.POST.get("first_name"),
						'last_name': request.POST.get("last_name"),
						'phone_number': request.POST.get("phone_number"),
						'username': request.POST.get("username"),
						'password': request.POST.get("password")
					}
				)
				user = user_form.save()
				user.set_password(password)
				customer = Customer(
					user=user,
					longitude=request.POST.get("longitude"),
					latitude=request.POST.get("latitude"),
					last_location_time=datetime.now()
				)
				customer.save()
				authenticate(username=username, password=password)
				pizza = Pizza.objects.get(id=request.POST["pizza_id"])
				pizza.customer = customer
				pizza.save()
				return HttpResponse(json.dumps({"was_bought": True}), content_type="application/json")
			else:
				return HttpResponse(json.dumps("Invalid params 1"), content_type="application/json")
	
	return HttpResponse(json.dumps("sorry"), content_type="application/json")



@login_required
def customer_dashboard(request):
	return render(request, 'customer-pizzas.html', {})
	
def anonymous_pizza_browser(request):
	if request.is_ajax() and request.method == 'POST':
		form = LocationForm(request.POST)
		if form.is_valid():
			unclaimed_pizzas = Pizza.objects.select_related().filter(customer__isnull=True)
			my_pizzas = Pizza.objects.select_related().filter(customer__user=request.user.id)
			close_pizzas = list()
			for pizza in list(unclaimed_pizzas) + list(my_pizzas):
				temp_pizza = dict()
				temp_pizza["pizza_id"] = pizza.id
				temp_pizza["cook_time"] = str(pizza.cook_time)
				temp_pizza["price"] =  str(pizza.price)
				temp_pizza["topping"] = pizza.get_topping_display()
				temp_pizza["driver_longitude"] = str(pizza.driver.longitude)
				temp_pizza["driver_latitude"] = str(pizza.driver.latitude)
				close_pizzas.append(temp_pizza)
				
			#TODO: sort the pizza by location, send distance rather than lat/long
			return HttpResponse(json.dumps(close_pizzas), content_type="application/json")
		else:
			return HttpResponse(json.dumps("sorry"), content_type="application/json")
	else:
		form = LocationForm()
		
	return render(request, 'anonymous-pizzas.html', {'form': form})

def add_pizza(request):
	if request.method == 'POST':
		if request.is_ajax():
			p = Pizza(
				topping=request.POST.get('topping').upper(),
				price=request.POST.get('price'),
				driver=Driver.objects.get(pk=1),
				cook_time=datetime.now()
			)			
			p.save()
			return HttpResponse( json.dumps({'victory': True}), content_type='application/json' )

@login_required
def deliver_pizza(request):
	if request.method == 'POST':
		if request.is_ajax():
			p = Pizza.objects.get(pk=request.POST['id'])
			p.delivered = True
			p.save()
			return HttpResponse( json.dumps({'victory': True}), content_type='application/json' )

@login_required
def driver_dashboard(request):
	pizzas_available = available_pizzas_as_dict(request.user.id)
	pizzas_delivered = pizza_to_dict(request.user.id, delivered=True)  # TODO: change this one to match the other two?
	pizzas_to_deliver = to_deliver_pizzas_as_dict(request.user.id)
	ctx = {'pizzas_available': pizzas_available, 'pizzas_delivered': pizzas_delivered, 'pizzas_to_deliver': pizzas_to_deliver }
	if request.is_ajax():
		return HttpResponse(render_to_string('driver-pizzas-ajax.html', ctx))
	else:
		return render(request, 'driver-pizzas.html', ctx)

def home(request):
	if request.user.is_authenticated():
		if len(list(Driver.objects.filter(user=request.user.id))) != 0:
			return HttpResponseRedirect('/driver/')
		else:
			return HttpResponseRedirect('/customer/')
	else:
		return HttpResponseRedirect('/pizzas/closest/')
	

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

def available_pizzas_as_dict(user_id):
	pizzas = []
	for i in Pizza.objects.select_related().filter(delivered=False).filter(driver__user_id=user_id).filter(customer=None).order_by('-cook_time'):
		pizzas.append({
			'cook_time': '%s -0400' % (i.cook_time), 
			'price': '$%.2f' % (i.price), 
			'topping': i.get_topping_display() 
		})
	return pizzas

def to_deliver_pizzas_as_dict(user_id):
	pizzas = []
	for i in Pizza.objects.select_related().filter(delivered=False).filter(driver__user_id=user_id).exclude(customer=None).order_by('-request_time'):
		full_or_user = i.customer.user.get_username()
		if i.customer:
			if i.customer.user.first_name and i.customer.user.last_name:
				full_or_user = '%s %s' % (i.customer.user.first_name, i.customer.user.last_name)		
		pizzas.append({
			'id': i.id,
			'customer_fullname_or_username': full_or_user,
			'topping': i.get_topping_display(),
			'price': '$%.2f' % (i.price),
			'request_time': '%s -0400' % (i.request_time),
			'customer_latitude': i.customer.latitude,
			'customer_longitude': i.customer.longitude,
			'customer_phone': i.customer.phone_number
		})
	return pizzas

def pizza_to_dict(user_id, customer=True, delivered=False):
	pizzas = list()
	
	for pizza in Pizza.objects.select_related().filter(delivered=delivered).filter(driver__user_id=user_id):
		formatted_pizza = dict()
		formatted_pizza["cook_time"] = '%s -0400' % (pizza.cook_time)
		formatted_pizza["price"] = '$%.2f' % (pizza.price)
		formatted_pizza["topping"] = pizza.get_topping_display()
		if pizza.request_time:
			formatted_pizza["request_time"] = '%s -0400' % (pizza.request_time)
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
