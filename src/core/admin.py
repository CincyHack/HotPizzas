from django.contrib import admin
from .models import Product, ProductConfiguration, Driver, Customer

admin.site.register(Product)
admin.site.register(ProductConfiguration)
admin.site.register(Driver)
admin.site.register(Customer)
