from rest_framework import viewsets
from ..models import Product, ProductType, ProductConfiguration, Driver, Customer
from ..serializers import ProductSerializer, ProductTypeSerializer, ProductConfigurationSerializer, DriverSerializer, CustomerSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductTypeViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = ProductType.objects.all()
	serializer_class = ProductTypeSerializer
	#lookup_field = 'name'

class ProductConfigurationViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = ProductConfiguration.objects.all()
	serializer_class = ProductConfigurationSerializer


class DriverViewSet(viewsets.ModelViewSet):
	queryset = Driver.objects.all()
	serializer_class = DriverSerializer
	

class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

