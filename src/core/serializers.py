from rest_framework import serializers
from .models import Product, ProductType, ProductConfiguration, Driver, Customer, CustomerInformation


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Customer
		fields = (
			'url',
			'phone_number',
			'products'
		)
		

class CustomerInformationSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = CustomerInformation
		fields = (
			'url',
			'name',
			'customer',
			'orders'
		)
		

class DriverSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Driver
		fields = (
			'url',
			'email',
			'phone_number',
			'products'
		)


class ProductSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Product
		fields = (
			'url',
			'cook_time',
			'expiration_time',
			'base_price',
			'delivered',
			'request_time',
			'customer',
			'configurations'
		)


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = ProductType
		fields = (
			'url',
			'name'
		)


class ProductConfigurationSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = ProductConfiguration
		fields = (
			'url',
			'description',
			'product_type'
		)

