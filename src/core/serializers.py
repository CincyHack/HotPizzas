from rest_framework import serializers
from .models import HotPizzasUser, Pizza

HotPizzasUserSerializer(serializers.HyperLinkedModelSerializer):
	class Meta:
		model = HotPizzasUser
		fields = ()

PizzaSerializer(serializers.HyperLinkedModelSerializer):
	class Meta:
		model = Pizza
		fields = ()
