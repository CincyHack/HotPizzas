#!/usr/bin/env python

from rest_framework import generics
from rest_framework import mixins
from ..serializers import ProductSerializer
from ..models import Product
from ..permissions import IsDriver, IsCustomer


class DriverUnsoldProductList(mixins.ListModelMixin, generic.GenericAPIView):
	serializer_class = ProuctSerializer
	queryset = Product.objects.filters(customer__isnull=True)


class DriverSoldProductList(mixins.ListModelMixin, generic.GenericAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.filters(customer__isnull=False)

	
class DriverUndeliveredProductList(mixins.ListModelMixin, generic.GenericAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.filters(delivered=False)

	
class DriverDeliveredProducList(mixins.ListModelMixin, generic.GenericAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.filters(delivered=True)
	

class DriverSoldUndeliveredProductList(mixins.ListModelMixin, generic.GenericAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.filters(delivered=False, customer__isnull=True)
