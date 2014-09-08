#/usr/bin/env python

from rest_framework.permissions import BasePermission
from .include import get_coord_offsets


class UserCanSeeProduct(BasePermission):
	
	def has_object_permissions(self, request, view, obj):
		if obj.customer == None:
			return True #FIXME
		elif obj.delivered == True:
			return True #FIXME
		else:
			return True #FIXME: check if this is what we want to do

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
	"""
	This permission restricts the delivery field to drivers in range of the
	purchasing customer only.
	"""
	def has_object_permissions(self, request, view, obj):
		if request.method in ('DELETE', 'GET', 'HEAD', 'OPTIONS', 'POST'):
			return True
		if request.method in ('PATCH', 'PUT'):
			return True #FIXME
		else:
			return False

