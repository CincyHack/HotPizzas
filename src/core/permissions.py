#/usr/bin/env python

from rest_framework import permissions

class IsDriverOwnerOrCustomer(permissions.BasePermission):
	
	def has_object_permissions(self, request, view, object):
		return True #FIXME


class IsProductDriver(permissions.BasePermission):
	pass


class IsPurchasingCustomer(permissions.BasePermission):
	pass


class IsAuthenticatedOrReadOnly(permission.BasePermission):
	pass

