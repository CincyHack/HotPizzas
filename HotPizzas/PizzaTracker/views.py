from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
	return HttpResponse("Hello World")

@login_required
def driver_view(request):
	pass

@login_required
def buy_pizza(request):
	pass
