from django.conf.urls import patterns, include, url

from django.contrib import admin
from core.views import (
	ProductViewSet,
	ProductTypeViewSet,
	ProductConfigurationViewSet,
	DriverViewSet,
	CustomerViewSet,
	LocationViewSet,
	LocalizedAvailableProductList,
)
from rest_framework.routers import DefaultRouter
admin.autodiscover()

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'product_type', ProductTypeViewSet)
router.register(r'product_configuration', ProductConfigurationViewSet)
router.register(r'driver', DriverViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'location', LocationViewSet)

urlpatterns = patterns('',
	url(r'^api/', include(router.urls)),
	url(r'^api/local/$', LocalizedAvailableProductList.as_view()),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
	url(r'^token/$', 'rest_framework_jwt.views.obtain_jwt_token'),
)

