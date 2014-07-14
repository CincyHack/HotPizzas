#!/usr/bin/env python

from rest_framework import generics
from rest_framework import mixins
from ..serializers import ProductSerializer
from ..models import Product
from ..permissions import IsDriver, IsCustomer


class DriverProductList(mixins.ListModelMixin, generic.GenericAPIView):
	serializer_class = ProuctSerializer

	def get_queryset(self):
		#add more filtering
		Product.objects.filters(sold=false)
