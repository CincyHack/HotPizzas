from rest_framework import status
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
		ProductPermission,
	)
	"""filter_backends = (DjangoObjectPermissionsFilter)"""
	base_name = "Unique"
	serializer_class = UniqueProductSerializer


	def get_queryset(self):
		return Product.objects.all()


	def list(self, request):
		(queryset, status) = self.get_filtered_set(request)
		serializer = self.serializer_class(queryset, many=True)	

		return Response(self.inject_eta(request, serializer.data), status=status)


	def get_filtered_set(self, request, pk=None):
		if pk:
			#FIXME: handle malformed strings, excessive configurations, etc - may need to do model work
			search_terms = pk.split("-")
			product_type = search_terms[0]
			configurations = search_terms[1:]
			filter_thresh = 5

			# Flag for 206 partial content return. 5 is arbitrary long call
			ret_status = status.HTTP_200_OK if (len(configurations) < filter_thresh) else status.HTTP_206_PARTIAL_CONTENT

			queryset = Product.objects.filter(product_type__name=product_type)
			queryset = queryset.filter(purchased=False)

			for configuration in configurations[:filter_thresh]:
				queryset = queryset.filter(configurations__description=configuration)

		else:
			#WARNING: this doesn't do what it looks like it does, but we try to do that below in a high complexity search
			queryset = Product.objects.order_by('product_type', 'base_price', 'configurations').distinct('product_type', 'base_price', 'configurations')
			queryset = queryset.filter(purchased=False)
			filtered_queryset = list()
			
			#FIXME: this is not sustainable
			for insert in queryset:
				if len(filtered_queryset) == 0:
					filtered_queryset.append(insert)
				else:
					exists = False
					for existing in filtered_queryset:
						if insert.base_price == existing.base_price and \
						insert.product_type == existing.product_type and \
						set(insert.configurations.all()) == set(existing.configurations.all()):
							exists = True
							break
						
					if not exists:
						filtered_queryset.append(insert)


			queryset = filtered_queryset
			ret_status = status.HTTP_200_OK

		return (queryset, ret_status)

	def get_eta(self, c_long, c_lat, p_long, p_lat):
		#FIXME: move this code elsewhere, to somewhere more generic
		#FIXME: currently fake number. fix when data gets better
		return 20

	def inject_eta(self, request, data):
		for index in range(len(data)):
			data[index]['eta'] = self.get_eta(0, 0, 0, 0) #FIXME: currently passing non values. Pass session when avail

		return data


	def retrieve(self, request, pk=None):
		
		if pk:
			(queryset, status) = self.get_filtered_set(request, pk)

			serializer = self.serializer_class(queryset, many=True)
			return Response(self.inject_eta(request, serializer.data), status=status)
		
		else:
			return Response([], status=status.HTTP_204_NO_CONTENT)


	def update(self, request, pk=None):
		if pk:
			(queryset, status) = self.get_filtered_set(request, pk)
			queryset = queryset.first()
			serializer = self.serializer_class(queryset)

			product_url = queryset.id
			#FIXME: actually buy that shiz
			return Response({"purchased_product": product_url})

		else:
			#FIXME: send a buy order
			return Response([])


class ProductViewSet(ModelViewSet):
	permission_classes = (
		ProductPermission,
	)
	"""filter_backends = (DjangoObjectPermissionsFilter)"""
	serializer_class = ProductSerializer
	model = Product

	def get_queryset(self):
		user = self.request.user
		if user.is_authenticated() and user.is_superuser:
			return Product.objects.filter(delivered=False)
		elif user.is_authenticated() and user.is_driver:
			return Product.objects.filter(delivered=False, driver=user)
		else:
			if 'sessionid' in self.request.COOKIES:
				sessionid = self.request.COOKIES.get('sessionid')
				return Product.objects.filter(delivered=False, purchased=False) #FIXME: query by sessionid
			else:
				return Product.objects.filter(delivered=False, purchased=False) 

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

	def list(self, request, *args, **kwargs):
		if request.user.is_authenticated()  and request.user.is_superuser:
			return super().list(request, *args, **kwargs)
		else:
			return Response({"error": "List view not allowed, use /unique/"}, status=status.HTTP_403_FORBIDDEN)
			

	def retrieve(self, request, *args, **kwargs):
		return super().retrieve(request, *args, **kwargs)


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
	
