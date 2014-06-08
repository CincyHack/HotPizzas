from django.views.generic.list import ListView
from ..models import Pizza

class PizzaListView(ListView):
	model = Pizza
