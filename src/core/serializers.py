from rest_framework import serializers
from .models import Product, ProductConfiguration, Driver, Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = ('url')

class DriverSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Driver
		fields = ('url')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ('url')


class ProductConfigurationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ProductConfiguration
		fields = ('url')

