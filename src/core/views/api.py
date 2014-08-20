from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
	CreateModelMixin,
	ListModelMixin,
	RetrieveModelMixin,
	UpdateModelMixin,
)
from ..models import (
	Product,
	ProductType,
	ProductConfiguration,
	Driver,
	Customer,
	CustomerInformation,
	Location,
)
from ..serializers import (
	ProductSerializer,
	ProductTypeSerializer,
	ProductConfigurationSerializer, 
	DriverSerializer, 
	CustomerSerializer,
	CustomerInformationSerializer,
	LocationSerializer,
)

class LocationViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer


class ProductViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductTypeViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
	queryset = ProductType.objects.all()
	serializer_class = ProductTypeSerializer


class ProductConfigurationViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
	queryset = ProductConfiguration.objects.all()
	serializer_class = ProductConfigurationSerializer


class DriverViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
	queryset = Driver.objects.all()
	serializer_class = DriverSerializer
	

class CustomerViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer


class CustomerInformationViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
	queryset = CustomerInformation.objects.all()
	serializer_class = CustomerInformationSerializer
