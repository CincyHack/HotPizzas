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

	class Meta:
		model = Product
		"""fields = (
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
			'product_type',
		)"""


class UniqueProductSerializer(serializers.Serializer):
	product_type = serializers.Field(source='product_type.name')
	configurations = serializers.SlugRelatedField(many=True, read_only=True, slug_field='description')

	class Meta:
		model = Product
		fields = (
			'product_type',
			'configurations',
		)

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):	

	class Meta:
		model = ProductType
		"""fields = (
			'url',
			'name',
		)"""


class ProductConfigurationSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = ProductConfiguration
		"""fields = (
			'url',
			'description',
		)"""

