#/usr/bin/env python
from rest_framework import BasePermission
from .include import get_coord_offsets


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


class DriverPermissionMixin(object):

	def is_driver(self, request):
		pass #TODO


	def is_product_driver(self, request, obj):
		pass #TODO


class CustomerPermissionMixin(object):

	def is_customer(self, request):
		pass #TODO

	def is_product_customer(self, request, obj):
		pass #TODO


class ProductPermission(SafeHTTPPermissionMixin, BasePermission):

	def has_pemissions(self, request, view):
		"""This should be overwritten by object permissions"""
		return False

	def has_object_permission(self, request, view, obj):
		return self.is_safe(request)


class UserPermission(SafeHTTPPermissionMixin, BasePermission):
	
	def has_permission(self, request, view):
		return False

	def has_object_permission(self, request, view, obj):
		return self.is_safe(request)


class ReadOnly(SafeHTTPPermissionMixin, BasePermission):

	def has_permission(self, request, view):
		return False

	def has_object_permission(self, request, view, obj):
		return self.is_safe(request)

