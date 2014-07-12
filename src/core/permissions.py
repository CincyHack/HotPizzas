#/usr/bin/env python

from rest_framework import permissions

class IsDriverOwnerOrCustomer(permissions.BasePermission):
	
	def has_object_permissions(self, request, view, object):
		return True #FIXME
