from rest_framework.permissions import (
	IsAuthenticatedOrReadOnly,
)
from rest_framework.viewsets import (
	ModelViewSet,
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
from ..permissions import (
	UserCanSeeProduct,
	IsProductDriver,
	IsPurchasingCustomer,
	UserIsInProductRange,
	UserIsInDeliveryRange,
)


class LocationViewSet(ModelViewSet):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer


class ProductViewSet(ModelViewSet):
	permission_classes = (
		UserCanSeeProduct,
		UserIsInProductRange,
		UserIsInDeliveryRange,
	)
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductTypeViewSet(ModelViewSet):
	queryset = ProductType.objects.all()
	serializer_class = ProductTypeSerializer


class ProductConfigurationViewSet(ModelViewSet):
	queryset = ProductConfiguration.objects.all()
	serializer_class = ProductConfigurationSerializer


class HotPizzasUserViewSet(ModelViewSet):
	queryset = HotPizzasUser.objects.all()
	serializer_class = HotPizzasUserSerializer

