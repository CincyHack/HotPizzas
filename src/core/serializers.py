from rest_framework import serializers
from .models import (
	HotPizzasUser,
	Product,
	ProductType,
	ProductConfiguration,
)

class HotPizzasUserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = HotPizzasUser
		fields = (
			'url',
			'is_customer',
			'is_driver',
			'phone_number',
			'name',
			'latitude',
			'longitude',
		)


class DriverSerializer(HotPizzasUserSerializer):
	pass


class CustomerSerializer(HotPizzasUserSerializer):
	pass


class ProductSerializer(serializers.HyperlinkedModelSerializer):

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
			'delivered_longitude',
			'delivered_latitude',
			'request_time',
			'driver',
		)


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):	

	class Meta:
		model = ProductType
		fields = (
			'url',
			'name',
		)


class ProductConfigurationSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = ProductConfiguration
		fields = (
			'url',
			'description',
		)

