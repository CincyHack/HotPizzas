#/usr/bin/env python
from rest_framework import BasePermission
from .include import get_coord_offsets


class ProductPermission(BasePermission):

	def has_pemissions(self, request, view):
		"""This should be overwritten by object permissions"""
		return False

	def has_object_permission(self, request, view, obj):
		return True



class UserPermission(BasePermission):
	
	def has_permission(self, request, view):
		return False

	def has_object_permission(self, request, view, obj):
		return True


class ReadOnly(BasePermission):

	def has_permission(self, request, view):
		return False

	def has_object_permission(self, request, view, obj):
		return True
