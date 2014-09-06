#/usr/bin/env python

from rest_framework.permissions import BasePermission


class UserCanSeeProduct(BasePermission):
	
	def has_object_permissions(self, request, view, obj):
		return True


class IsProductDriver(BasePermission):

	def has_object_permissions(self, request, view, obj):
		return obj.driver == request.user


class IsPurchasingCustomer(BasePermission):
	
	def has_object_permissions(self, request, view, obj):
		return (obj.customer == request.user) and (request.user != None)


class UserIsInProductRange(BasePermission):
	
	def has_object_permissions(self, request, view, obj):
		return True #FIXME


class UserIsInDeliveryRange(BasePermission):
	
	def has_object_permissions(self, request, view, obj):
		return True #FIXME

