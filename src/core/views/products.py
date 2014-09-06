#!/usr/bin/env python
from django.utils import timezone
from rest_framework.mixins import (
	ListModelMixin
)
from rest_framework import (
	views,
	generics,
	status,
)
from rest_framework.response import Response
from ..serializers import ProductSerializer
from ..models import Product, HotPizzasUser
from ..include import get_coord_offsets

class CustomerFilterMixin(object):
	
	def filter_customer(self):
		customer = self.request.user
		return Product.objects.filter(customer=customer)
		
		
class CustomerUndeliveredProductList(CustomerFilterMixin, ListModelMixin, generics.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		queryset = self.filter_customer()
		return queryset.filter(delivered__isnull=True)
		
		
class LocalizedAvailableProductList(views.APIView):

	def get(self, request, format=None):
		if 'longitude' in request.GET and 'latitude' in request.GET:
			longitude = float(request.GET.get('longitude'))
			latitude = float(request.GET.get('latitude'))
			(long_max, long_min, lat_max, lat_min) = get_coord_offsets(
				longitude,
				latitude,
				10,
				'm'
			)
			products = Product.objects.filter(
				location__longitude__gte=long_min,
				location__longitude__lte=long_max,
				location__latitude__gte=-lat_min,
				location__latitude__lte=lat_max,
				customer__isnull=True,
				expiration_time__gt=timezone.now()
			)
			serializer = ProductSerializer(products, many=True, context={'request':request})
			return Response(serializer.data)
		else: # Either longitude or latitude aren't in the request queryset
			return Response(
				{'details':'longitude and latitude must be defined in query string. Try adding ?longitude=0.0&latitude=0.0'},
				status=status.HTTP_400_BAD_REQUEST,
			)	
		

class DriverFilterMixin(object):
	
	def filter_driver(self):
		driver = self.request.user
		return Product.objects.filter(driver=driver)


class DriverUnsoldProductList(DriverFilterMixin, ListModelMixin, generics.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		queryset = self.filter_driver()
		return queryset.filter(customer__isnull=True)


class DriverSoldProductList(DriverFilterMixin, ListModelMixin, generics.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		queryset = self.filter_driver()
		return queryset.filter(customer__isnull=False)

	
class DriverUndeliveredProductList(DriverFilterMixin, ListModelMixin, generics.GenericAPIView):
	serializer_class = ProductSerializer

	def get_queryset(self):
		queryset = self.filter_driver()
		return queryset.filter(delivered=False)

	
class DriverDeliveredProducList(DriverFilterMixin, ListModelMixin, generics.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		queryset = self.filter_driver()
		return queryset.filter(delivered=True)
	

class DriverSoldUndeliveredProductList(DriverFilterMixin, ListModelMixin, generics.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		queryset = self.filter_driver()
		return queryset.filter(delivered=False, customer__isnull=True)

