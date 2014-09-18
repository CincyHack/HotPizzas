#/usr/bin/env python
from rest_framework import BasePermission
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
		return request.method = 'PATCH'


class PostPermissionMixin(object):

	def is_post(self, request):
		return requst.method == 'POST'


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
	self.is_create = self.is_post


class RetrievePermissionMixin(GetPermissionMixin):
	"""CRUD/REST macro to HTTP"""
	self.is_retrieve = self.is_get


class PartialUpdatePermissionMixin(PatchPermissionMixin):
	"""CRUD/REST macro to HTTP"""
	self.is_partial_update = self.is_patch


class FullUpdatePermissionMixin(PutPermissionMixin):
	"""CRUD/REST macro to HTTP"""
	self.is_full_update = self.is_put


class UpdatePermissionMixin(PartialUpdatePermissionMixin, FullUpdatePermissionMixin):
	"""CRUD/REST macro of Partial and Full Update"""
	def is_update(self, request):
		return self.is_partial_update(request) or self.is_full_update(request)


class DestroyPermissionMixin(DeletePermissionMixin):
	"""CRUD/REST macro to HTTP"""
	self.is_destroy = self.destroy


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
			if isinstance(obj, Product)
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


class ProductPermission(RESTPermissionMixin, BasePermission):

	def has_pemissions(self, request, view):
		"""This should be overwritten by object permissions"""
		return False

	def has_object_permission(self, request, view, obj):
		if self.is_create(request):
			return True
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


class UserPermission(RESTPermissionMixin, DriverPermissionMixin, BasePermission):
	
	def has_permission(self, request, view):
		"""This should be overwritten by object permissions"""
		return False

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


class ReadOnly(SafeHTTPPermissionMixin, BasePermission):

	def has_permission(self, request, view):
		return False

	def has_object_permission(self, request, view, obj):
		return self.is_safe(request)

