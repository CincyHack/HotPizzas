from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
	CreateModelMixin,
	ListModelMixin,
	RetrieveModelMixin,
	UpdateModelMixin,
)
from ..models import (
	HotPizzasUser,
	Product,
	ProductType,
	ProductConfiguration,
	Location,
)
from ..serializers import (
	HotPizzasUserSerializer,
	ProductSerializer,
	ProductTypeSerializer,
	ProductConfigurationSerializer, 
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


class HotPizzasUserViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
	queryset = HotPizzasUser.objects.all()
	serializer_class = HotPizzasUserSerializer

