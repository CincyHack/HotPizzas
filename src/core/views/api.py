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
	ReadOnly,
	IsAdminOrReadOnly,
	ProductPermission,
	UserPermission,
)


class ProductViewSet(ModelViewSet):
	permission_classes = (
		ProductPermission,
	)
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductTypeViewSet(ModelViewSet):
	permission_classes = (
		ReadOnly,
	)
	queryset = ProductType.objects.all()
	serializer_class = ProductTypeSerializer


class ProductConfigurationViewSet(ModelViewSet):
	permission_classes = (
		ReadOnly,
	)
	queryset = ProductConfiguration.objects.all()
	serializer_class = ProductConfigurationSerializer


class HotPizzasUserViewSet(ModelViewSet):
	permission_classes = (
		UserPermission,
	)
	queryset = HotPizzasUser.objects.all()
	serializer_class = HotPizzasUserSerializer

