#/usr/bin/env python
from rest_framework.permissions import (
	BasePermission,
	DjangoObjectPermissions,
)
from .include import get_coord_offsets
from .models import Product


class DeletePermissionMixin(object):

	def is_delete(self, request):
		return request.method == 'DELETE'


class GetPermissionMixin(object):

	def is_get(self, request):
		return request.method == 'GET'


class PatchPermissionMixin(object):

	def is_patch(self, request):
		return request.method == 'PATCH'


class PostPermissionMixin(object):

	def is_post(self, request):
		return request.method == 'POST'


class PutPermissionMixin(object):

	def is_put(self, request):
		return request.method == 'PUT'


class SafeHTTPPermissionMixin(object):

	def is_safe(self, request):
		return request.method in ['GET', 'OPTIONS', 'HEAD']


class HTTPPermissionMixin(
	DeletePermissionMixin,
	GetPermissionMixin,
	PatchPermissionMixin,
	PostPermissionMixin,
	PutPermissionMixin,
	SafeHTTPPermissionMixin,
):
	"""This mixin is a macro."""
	pass


class CreatePermissionMixin(PostPermissionMixin):
	"""CRUD/REST macro to HTTP"""
	def is_create(self, request):
		return self.is_post(request)


class RetrievePermissionMixin(GetPermissionMixin):
	"""CRUD/REST macro to HTTP"""
	def is_retrieve(self, request):
		return self.is_get(request)


class PartialUpdatePermissionMixin(PatchPermissionMixin):
	"""CRUD/REST macro to HTTP"""
	def is_partial_update(self, request):
		return self.is_patch(request)


class FullUpdatePermissionMixin(PutPermissionMixin):
	"""CRUD/REST macro to HTTP"""
	def is_full_update(self, request):
		return  self.is_put(request)


class UpdatePermissionMixin(PartialUpdatePermissionMixin, FullUpdatePermissionMixin):
	"""CRUD/REST macro of Partial and Full Update"""
	def is_update(self, request):
		return self.is_partial_update(request) or self.is_full_update(request)


class DestroyPermissionMixin(DeletePermissionMixin):
	"""CRUD/REST macro to HTTP"""
	def is_destroy(self, request):
		return self.is_delete(request)


class RESTPermissionMixin(
	HTTPPermissionMixin,
	CreatePermissionMixin,
	RetrievePermissionMixin,
	UpdatePermissionMixin,
	DestroyPermissionMixin,
):
	"""This mixin is a macro."""
	pass


#Alias CRUD and REST
CRUDPermissionMixin = RESTPermissionMixin


class DriverPermissionMixin(object):

	def is_driver(self, request):
		if request.user.is_authenticated():
			return request.user.is_driver
		else:
			return False


	def is_product_driver(self, request, obj):
		if self.is_driver(request):
			if isinstance(obj, Product):
				return request.user == obj.driver
			else:
				return False
		else:
			return False


class CustomerPermissionMixin(object):

	def is_customer(self, request):
		if request.user.is_authenticated():
			return request.user.is_customer
		else:
			return False

	def is_product_customer(self, request, obj):
		if self.is_customer(request):
			if isinstance(obj, Product):
				return request.user == obj.customer
			else:
				return False
		else:
			return False


class ProductPermission(DriverPermissionMixin, RESTPermissionMixin, BasePermission):

	perms_map = {
		'GET': ['%(app_label)s.view_%(model_name)s'],
		'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
		'HEAD': ['%(app_label)s.view_%(model_name)s'],
		'POST': ['%(app_label)s.add_%(model_name)s'],
		'PUT': ['%(app_label)s.change_%(model_name)s'],
		'PATCH': ['%(app_label)s.change_%(model_name)s'],
		'DELETE': ['%(app_label)s.delete_%(model_name)s'],
	}

	def has_object_permission(self, request, view, obj):
		if self.is_create(request):
			return self.is_driver(request)
		elif self.is_retrieve(request):
			return True #FIXME: this is leaky, especially for purchased products
		elif self.is_update(request):
			return False #FIXME: users should be able to update products to purchase, drivers should be able to fix pizza
		elif self.is_destroy(request):
			return False #FIXME: drivers should be able to remove an incorrect pizza
		elif self.is_safe(request):
			return True
		else:
			return False


class UserPermission(RESTPermissionMixin, DriverPermissionMixin, DjangoObjectPermissions):

	perms_map = {
		'GET': ['%(app_label)s.view_%(model_name)s'],
		'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
		'HEAD': ['%(app_label)s.view_%(model_name)s'],
		'POST': ['%(app_label)s.add_%(model_name)s'],
		'PUT': ['%(app_label)s.change_%(model_name)s'],
		'PATCH': ['%(app_label)s.change_%(model_name)s'],
		'DELETE': ['%(app_label)s.delete_%(model_name)s'],
	}
"""
	def has_object_permission(self, request, view, obj):
		if self.is_create(request):
			return True
		elif self.is_retrieve(request):
			return True #FIXME: this is leaky, especially for location data
		elif self.is_update(request):
			return False #FIXME: users should be able to update themselves
		elif self.is_destroy(request):
			return False #FIXME: users should be able to set themselves to inactive
		elif self.is_safe(request):
			return True
		else:
			return False
"""


class ReadOnly(SafeHTTPPermissionMixin, BasePermission):

	def has_permission(self, request, view):
		return self.is_safe(request)

	def has_object_permission(self, request, view, obj):
		return self.is_safe(request)

