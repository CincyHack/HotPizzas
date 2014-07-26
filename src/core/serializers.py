from rest_framework import serializers
from .models import (
	Product,
	ProductType,
	ProductConfiguration,
	Driver,
	Customer,
	CustomerInformation,
	Location
)

class LocationSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Location
		fields = (
			'longitude',
			'latitude'
		)


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Customer
		fields = (
			'url',
			'phone_number',
			'customer_informations'
		)
		

class CustomerInformationSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = CustomerInformation
		fields = (
			'url',
			'name',
			'customer',
			'products',
			'location'
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

	longitude = serializers.Field(source='location.longitude')
	latitude = serializers.Field(source='location.latitude')
	configurations= serializers.RelatedField(many=True)

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
			'configurations',
			'longitude',
			'latitude',
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

