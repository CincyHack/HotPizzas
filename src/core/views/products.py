#!/usr/bin/env python

from rest_framework import generics
from rest_framework import mixins
from ..serializers import ProductSerializer
from ..models import Product, CustomerInformation, Customer
from ..permissions import IsDriver, IsCustomer
from ..include import get_coord_offsets

class CustomerFilterMixin(object):
	
	def filter_customer(self):
		customer = self.request.user
		return Product.objects.filter(customer__user=customer)
		
		
class CustomerUndeliveredProductList(CustomerFilterMixin, mixins.ListModelMixin, generics.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		queryset = filter_customer()
		return queryset.filter(delivered__isnull=True)
		
		
class LocalizedAvailableProductList(mixins.ListModelMixin, generics.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		longitude = self.request.longitude
		latitude = self.request.latitude
		(long_min, long_max, lat_min, lat_max) = get_coord_offsets(
			longitude,
			latitude,
			10,
			'm'
		)
		return Product.objects.filter(
			location__longitude__gte=long_min,
			location__longitude__lte=long_max,
			location__latitude__gte=lat_min,
			location__latiude__lte=lat_max
		)
		

class DriverFilterMixin(object):
	
	def filter_driver(self):
		driver = self.request.user
		return Product.objects.filter(driver__user=driver)


class DriverUnsoldProductList(DriverFilterMixin, mixins.ListModelMixin, generics.GenericAPIView):
	serializer_class = ProuctSerializer
	
	def get_queryset(self):
		queryset = filter_driver()
		return queryset.filter(customer__isnull=True)


class DriverSoldProductList(DriverFilterMixin, mixins.ListModelMixin, generics.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		queryset = filter_driver()
		return queryset.filter(customer__isnull=False)

	
class DriverUndeliveredProductList(DriverFilterMixin, mixins.ListModelMixin, generics.GenericAPIView):
	serializer_class = ProductSerializer

	def get_queryset(self):
		queryset = filter_driver()
		return queryset.filter(delivered=False)

	
class DriverDeliveredProducList(DriverFilterMixin, mixins.ListModelMixin, generics.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		queryset = filter_driver()
		return queryset.filter(delivered=True)
	

class DriverSoldUndeliveredProductList(DriverFilterMixin, mixins.ListModelMixin, generics.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		queryset = filter_driver()
		return queryset.filter(delivered=False, customer__isnull=True)

