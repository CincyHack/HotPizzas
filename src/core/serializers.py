from rest_framework import serializers
from .models import Product, ProductConfiguration, Driver, Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	products = serilizers.HyperlinkedRelatedField(view_name='product-detail', many=True)
	
	class Meta:
		model = Customer
		fields = ('url', 'phone_number', 'products')

class DriverSerializer(serializers.HyperlinkedModelSerializer):
	products = serializers.HyperlinkedRelatedField(view_name='product-detail', many=True)
	
	class Meta:
		model = Driver
		fields = ('url', 'email', 'phone_number', 'products')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	product_configurations = serializers.HyperlinkedRelatedField(view_name='product_configuration-details', many=True)
	
	class Meta:
		model = Product
		fields = ('url', 'cook_time', 'expiration_time', 'base_price', 'delivered', 'request_time', 'product_configurations')


class ProductConfigurationSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = ProductConfiguration
		fields = ('url', 'description')

