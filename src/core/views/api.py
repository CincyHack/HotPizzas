from rest_framework.viewsets import (
	ModelViewSet,
)
from rest_framework.filters import (
	DjangoObjectPermissionsFilter,
)
from rest_framework.permissions import (
	AllowAny
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
	ProductPermission,
	UserPermission,
)


class ProductViewSet(ModelViewSet):
	permission_classes = (
		ProductPermission,
	)
	"""filter_backends = (
		DjangoObjectPermissionsFilter,
	)"""
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def buy(self, request, *args, **kwargs):
		pass

	def deliver(self, request, *args, **kwargs):
		pass

	def update(self, request, *args, **kwargs):
		return super().update(request, *args, **kwargs)

	def create(self, request, *args, **kwargs):
		return super().create(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return super().delete(request, *args, **kwargs)


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
	filter_backends = (
		DjangoObjectPermissionsFilter,
	)
	queryset = HotPizzasUser.objects.all()
	serializer_class = HotPizzasUserSerializer
	
	def update(self, request, *args, **kwargs):
		return super().update(request, *args, **kwargs)

	def create(self, request, *args, **kwargs):
		return super().create(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return super().delete(request, *args, **kwargs)
	
