from rest_framework.viewsets import (
	GenericViewSet,
	ModelViewSet,
)
from rest_framework.filters import (
	DjangoObjectPermissionsFilter,
)
from rest_framework.permissions import (
	AllowAny,
)
from rest_framework.response import (
	Response,
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
	UniqueProductSerializer,
)
from ..permissions import (
	ReadOnly,
	ProductPermission,
	UserPermission,
)


class UniqueProductViewSet(GenericViewSet):
	permission_classes = (
		AllowAny,
	)	
	queryset = Product.objects.all()
	serializer_class = UniqueProductSerializer

	def list(self, request):
		serializer = self.serializer_class(self.queryset, many=True)
		return Response(serializer.data)

	def create(self, request):
		return Response([])

	def retrieve(self, request, pk=None):
		
		if pk:
			#FIXME: handle malformed strings, excessive configurations, etc - may need to do model work
			search_terms = pk.split("-")
			product_type = search_terms[0]
			configurations = search_terms[1:]
			#TODO: make sure to filter unclaimed, unpurchased
			query = Product.objects.filter(product_type__name=product_type)
			query.filter(configurations__description__in=configurations)
			queryset = query.first()
			serializer = self.serializer_class(queryset)
			return Response(serializer.data)
		
		else:
			return Response([]) #FIXME consider returning a 404 or some error


	def update(self, request, pk=None):
		return Response([])


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
	
