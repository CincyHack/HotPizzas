from rest_framework import viewsets
from ..models import Product, ProductConfiguration, Driver, Customer
from ..serializers import ProductSerializer, ProductConfigurationSerializer, DriverSerializer, CustomerSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ProductConfigurationViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = ProductConfiguration.objects.all()
	serializer_class = ProductConfigurationSerializer

class DriverViewSet(viewsets.ModelViewSet):
	queryset = Driver.objects.all()
	serializer_class = Driver
	

class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = Customer


