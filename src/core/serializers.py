from rest_framework import serializers
from rest_framework.reverse import reverse_lazy
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


class UniqueProductSerializer(serializers.ModelSerializer):
	product_type = serializers.Field(source='product_type.name')
	configurations = serializers.SlugRelatedField(many=True, read_only=True, slug_field='description')
	url = serializers.SerializerMethodField('get_unique_url')

	def get_unique_url(self, obj):
		#FIXME: change the url to not be hardcoded
		config_string = ""
		for each in obj.configurations.all():
			config_string = config_string + "-" + str(each.description)

		return "http://hotpizzas.co/api/unique/{0}{1}".format(obj.product_type.name, config_string)


	class Meta:
		model = Product
		fields = (
			'url',
			'product_type',
			'configurations',
			'base_price',
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

