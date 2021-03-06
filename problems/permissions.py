from rest_framework import permissions


class IsAuthorOrAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff


class IsAuthorOrReservedProblemInvisable(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.reserved == True:
            return (obj.author == request.user) or request.user.is_staff
        return True
