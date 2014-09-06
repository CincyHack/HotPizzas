from rest_framework.permissions import (
	AllowAny,
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
	permission_classes = (
		AllowAny,
	)
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
	permission_classes = (
		AllowAny,
	)
	queryset = ProductType.objects.all()
	serializer_class = ProductTypeSerializer


class ProductConfigurationViewSet(ModelViewSet):
	permission_classes = (
		AllowAny,
	)
	queryset = ProductConfiguration.objects.all()
	serializer_class = ProductConfigurationSerializer


class HotPizzasUserViewSet(ModelViewSet):
	permission_classes = (
		AllowAny,
	)
	queryset = HotPizzasUser.objects.all()
	serializer_class = HotPizzasUserSerializer

