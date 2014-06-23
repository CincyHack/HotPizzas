from rest_framework import serializers
from .models import Product, ProductConfiguration, Driver, Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = ('url', 'phone_number')

class DriverSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Driver
		fields = ('url', 'email', 'phone_number')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ('url', 'cook_time', 'expiration_time', 'base_price', 'delivered', 'request_time')


class ProductConfigurationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ProductConfiguration
		fields = ('url', 'description')

