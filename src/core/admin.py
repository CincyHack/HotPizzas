from django.contrib import admin
from .models import (
	Product,
	ProductType,
	ProductConfiguration,
	Driver,
	Customer,
	CustomerInformation,
	Location,
)

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductConfiguration)
admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(CustomerInformation)
admin.site.register(Location)
