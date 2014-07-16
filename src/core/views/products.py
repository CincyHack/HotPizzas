#!/usr/bin/env python

from rest_framework import generics
from rest_framework import mixins
from ..serializers import ProductSerializer
from ..models import Product
from ..permissions import IsDriver, IsCustomer


class DriverUnsoldProductList(mixins.ListModelMixin, generic.GenericAPIView):
	serializer_class = ProuctSerializer
	
	def get_queryset(self):
		driver = self.request.driver
		return Product.objects.filter(customer__isnull=True, driver=driver)


class DriverSoldProductList(mixins.ListModelMixin, generic.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		driver = self.request.driver
		return Product.objects.filter(customer__isnull=False)

	
class DriverUndeliveredProductList(mixins.ListModelMixin, generic.GenericAPIView):
	serializer_class = ProductSerializer

	def get_queryset(self):
		driver = self.request.driver
		return Product.objects.filter(delivered=False)

	
class DriverDeliveredProducList(mixins.ListModelMixin, generic.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		driver = self.request.driver
		return Product.objects.filter(delivered=True)
	

class DriverSoldUndeliveredProductList(mixins.ListModelMixin, generic.GenericAPIView):
	serializer_class = ProductSerializer
	
	def get_queryset(self):
		driver = self.request.driver
		return Product.objects.filter(delivered=False, customer__isnull=True)
