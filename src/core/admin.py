from django.contrib import admin
from .models import (
	Product,
	ProductType,
	ProductConfiguration,
	HotPizzasUser,
	Location,
)

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductConfiguration)
admin.site.register(HotPizzasUser)
admin.site.register(Location)
