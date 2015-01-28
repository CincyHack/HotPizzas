from rest_framework import (
	views,
)
from rest_framework.status import (
	HTTP_200_OK,
	HTTP_204_NO_CONTENT,
    HTTP_206_PARTIAL_CONTENT,
	HTTP_400_BAD_REQUEST,
)
from rest_framework.response import Response
from ..models import (
	Product,
	ProductConfiguration,
)
from ..include import (
	parse_filter,
	get_coord_offsets,
	get_user_gps,
	est_time,
	is_valid_geo,
)

class UniqueProductView(views.APIView):

	def get(self, request, filter=None, format=None):
		(product_type, configs) = parse_filter(filter)

		user_gps = get_user_gps(request)
		(lon, lat) = user_gps
		if not lon or not lat:
			return Response(
				{"details": "Need lat and lon in get params"},
				status=HTTP_400_BAD_REQUEST,)
		elif not is_valid_geo(lon) or not is_valid_geo(lat)
			return Response(
				{"details": "Lat and lon must be numeric"},
				status=HTTP_400_BAD_REQUEST,)

		(long_high, long_low, lat_high, lat_low) =\
			get_coord_offsets(lon, lat, 10, 'mi')

		product_set = Product.objects.filter(
			purchased=False,
			driver_longitude__lte=long_high,
			driver_longitude__gte=long_low,
			driver_latitude__lte=lat_high,
			driver_latitude__gte=lat_low,
		)

		if product_type:
			product_set = product_set.filter(product_type__name=product_type)
			config_set = ProductConfiguration.objects.filter(
				product_type=product_type,
				description__in=configs,
			)
			for config in config_set:
				product_set = product_set.filter(configuration=config)

		unique = []
		for product in product_set:
			prod_configs = [config.description for config in product.configurations.all()]
			prod_gps = (product.driver.longitude, prouct.driver.latitude)
			prod_config_set = set(prod_configs)

			if len(unique) is 0:
				unque.append({
					"price": str(product.price),
					"configurations": prod_configs,
					"configuration_set": prod_config_set,
					"product_type": product.product_type,
					"eta": est_time(user_gps, prod_gps),
					"count": 1,
				})
			else:
				matched = False
				for item in unique:
					if (item.get("configuration_set", set()) ^ prod_config_set) is 0: #Sets are equivalent
						if float(item.get("price", "inf")) > float(product.price):
							item["price"] = str(product.price)
							item["eta"] = est_time(user_gps, prod_gps, old=item.get("eta", None), count=item.get("count", 0))
							item["count"] = item.get("count", 0) + 1

						matched = True
						break

		for elem in unique:
			elem.pop("count", None)
			elem.pop("configurations_set", None)

		return Response(unique, status=HTTP_200_OK)


	def post(self, request, filter=None, format=None):
		pass

