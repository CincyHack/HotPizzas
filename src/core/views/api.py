from rest_framework import viewsets
from rest_framework import mixins
from ..models import (
	Product,
	ProductType,
	ProductConfiguration,
	Driver,
	Customer,
	CustomerInformation,
	Location
)
from ..serializers import (
	ProductSerializer,
	ProductTypeSerializer,
	ProductConfigurationSerializer, 
	DriverSerializer, 
	CustomerSerializer,
	CustomerInformationSerializer,
	LocationSerializer
)

class LocationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer


class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductTypeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	queryset = ProductType.objects.all()
	serializer_class = ProductTypeSerializer


class ProductConfigurationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	queryset = ProductConfiguration.objects.all()
	serializer_class = ProductConfigurationSerializer


class DriverViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	queryset = Driver.objects.all()
	serializer_class = DriverSerializer
	

class CustomerViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer


class CustomerInformationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	queryset = CustomerInformation.objects.all()
	serializer_class = CustomerInformationSerializer
