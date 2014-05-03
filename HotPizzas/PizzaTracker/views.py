from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def driver_view(request):
	pass

@login_required
def buy_pizza(request):
	pass
