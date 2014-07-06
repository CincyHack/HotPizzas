from django.conf.urls import patterns, include, url

from django.contrib import admin
from core.views import ProductViewSet, ProductTypeViewSet, ProductConfigurationViewSet, DriverViewSet, CustomerViewSet
from rest_framework.routers import DefaultRouter
admin.autodiscover()

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'product_type', ProductTypeViewSet)
router.register(r'product_configuration', ProductConfigurationViewSet)
router.register(r'driver', DriverViewSet)
router.register(r'customer', CustomerViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #/login/ to sign in to the application
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    #/logout/ to sign out of the application
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'login.html'}),
)

