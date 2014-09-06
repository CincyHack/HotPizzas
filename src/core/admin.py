from django.contrib import admin
from .models import (
	Product,
	ProductType,
	ProductConfiguration,
	HotPizzasUser,
)

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductConfiguration)
admin.site.register(HotPizzasUser)
