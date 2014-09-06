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
)
from ..serializers import (
	HotPizzasUserSerializer,
	ProductSerializer,
	ProductTypeSerializer,
	ProductConfigurationSerializer, 
)
from ..permissions import (
	UserCanSeeProduct,
	IsProductDriver,
	IsPurchasingCustomer,
	UserIsInProductRange,
	UserIsInDeliveryRange,
)


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

