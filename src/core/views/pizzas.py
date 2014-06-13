from django.views.generic.list import ListView
from ..models import Pizza

class PizzaListView(ListView):
	model = Pizza

class AvailablePizzaListView(PizzaListView):
	pass

class DriverPizzaListView(PizzaListView):
	pass

